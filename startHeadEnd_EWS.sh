clear

sudo sh /home/tvdigital/Desktop/LinuxSDK/Dta1xx/Dta1xxInit stop
sudo sh /home/tvdigital/Desktop/LinuxSDK/Dta1xx/Dta1xxInit start

export SITemp=./Temp/SITemp
export AVRef=./AVRef
export OC1Dir=./OC/oc1

export OC1Output=./Temp/OCTemp/oc1.ts
export OC1Version=1

# oc-update.sh object_carousel_directory association_tag module_version dsmcc_pid carousel_id [compress_on]
oc-update-output.sh $OC1Dir 0xB $OC1Version 2003 1 $OC1Output 1 0 0

# Load konfigurasi
#./mptsconfig.py
./mptsconfig_ews.py &

# Alokasi file Pipe file untuk 6 siaran (video/audio)
/usr/bin/mkfifo ./av1ts.pipe &
/usr/bin/mkfifo ./av2ts.pipe &
/usr/bin/mkfifo ./av3ts.pipe &
/usr/bin/mkfifo ./av4ts.pipe &
/usr/bin/mkfifo ./av5ts.pipe &
/usr/bin/mkfifo ./av6ts.pipe &

#/usr/bin/mkfifo ./nullts.pipe

# Alokasi file pipe untuk PSI tabel
/usr/bin/mkfifo ./finalav.pipe &
/usr/bin/mkfifo ./finalavnull.pipe &
/usr/bin/mkfifo ./final.pipe &
/usr/bin/mkfifo ./finaltdt.pipe &
/usr/bin/mkfifo ./finalstamp.pipe &


#/usr/bin/mkfifo ./av1.pipe
#/usr/bin/mkfifo ./av2.pipe
#/usr/bin/mkfifo ./av3.pipe
#/usr/bin/mkfifo ./av4.pipe
#/usr/bin/mkfifo ./av5.pipe
#/usr/bin/mkfifo ./av6.pipe

/usr/bin/mkfifo ./nit.pipe &
/usr/bin/mkfifo ./pat.pipe &

/usr/bin/mkfifo ./pmt0.pipe &
/usr/bin/mkfifo ./pmt1.pipe &
/usr/bin/mkfifo ./pmt2.pipe &
/usr/bin/mkfifo ./pmt3.pipe &
/usr/bin/mkfifo ./pmt4.pipe &
/usr/bin/mkfifo ./pmt5.pipe &

/usr/bin/mkfifo ./sdt.pipe &
/usr/bin/mkfifo ./tdt.pipe &
#/usr/bin/mkfifo ./eit.pipe

# EWS
/usr/bin/mkfifo ./ewspmt.pipe &
/usr/bin/mkfifo ./ewsit.pipe  &
/usr/bin/mkfifo ./ewscountry.pipe &
/usr/bin/mkfifo ./ewsregion.pipe &
/usr/bin/mkfifo ./ewslocation.pipe &
/usr/bin/mkfifo ./ewspriority.pipe &
/usr/bin/mkfifo ./ewsdisaster.pipe &
/usr/bin/mkfifo ./ewsmessage.pipe &
/usr/bin/mkfifo ./ewsfinal.pipe &

/usr/bin/mkfifo ./oc1.pipe &

/usr/bin/mkfifo ./ait0.pipe &

# Load Transport Stream ke dalam file Piping 
tsloop ./AVRef/IPMAN2.ts > ./av1.pipe &
tsloop ./AVRef/IND-DEMO2a.ts > ./av2.pipe &
tsloop ./AVRef/IND-DEMO3a.ts > ./av3.pipe &
tsloop ./AVRef/IND-DEMO4a.ts > ./av4.pipe &
tsloop ./AVRef/IND-DEMO5a.ts > ./av5.pipe &
#tsloop ./AVRef/IND-DEMO6z.ts > ./av6.pipe &

#tsloop ./AVRef/IND-DEMO6a.ts > ./av6.pipe &
#tsloop ./TSRef/null.ts > ./nullts.pipe &
#tsfilter ./av1ts.pipe +35 +36 > ./av1.pipe &
#tsfilter ./av2ts.pipe +40 +41 > ./av2.pipe &
#tsfilter ./av3ts.pipe +45 +46 > ./av3.pipe &
#tsfilter ./av4ts.pipe +50 +51 > ./av4.pipe &
#tsfilter ./av5ts.pipe +55 +56 > ./av5.pipe &
#tsfilter ./av6ts.pipe +60 +61 > ./av6.pipe &

tsloop $SITemp/pat.ts > ./pat.pipe &
tsloop $SITemp/nit.ts > ./nit.pipe &

tsloop $SITemp/pmt0.ts > ./pmt0.pipe &
tsloop $SITemp/pmt1.ts > ./pmt1.pipe &
tsloop $SITemp/pmt2.ts > ./pmt2.pipe &
tsloop $SITemp/pmt3.ts > ./pmt3.pipe &
tsloop $SITemp/pmt4.ts > ./pmt4.pipe &
tsloop $SITemp/pmt5.ts > ./pmt5.pipe &

tsloop $SITemp/sdt.ts > ./sdt.pipe &
tsloop $SITemp/tdt.ts > ./tdt.pipe &
#tsloop $SITemp/eit.ts > ./eit.pipe &

tsloop $SITemp/ait0.ts > ./ait0.pipe &
tsloop $OC1Output  > ./oc1.pipe &

tsloop $SITemp/ewspmt.ts > ./ewspmt.pipe &
tsloop $SITemp/ewsit.ts > ./ewsit.pipe &
tsloop $SITemp/ewsmessage.ts > ./ewsmessage.pipe &

# Muxing EWS : TODO: tsudpreceive 
tscbrmuxer  b:10000 ./ewsit.pipe b:10000 ./ewsmessage.pipe b:10000 ./ewspmt.pipe > ./ewsfinal.pipe &

# Muxing EWS + Video
#tscbrmuxer b:10000 ./eit.pipe b:500000 ./oc1.pipe b:100000 ./ewsfinal.pipe b:3195568 ./av1.pipe b:3195338 ./av2.pipe b:3196003 ./av3.pipe b:3196662 ./av4.pipe b:3197586 ./av5.pipe b:3197586 ./av6.pipe  > ./finalav.pipe &

#tscbrmuxer b:500000 ./oc1.pipe b:100000 ./ewsfinal.pipe b:3195568 ./av1.pipe b:3195338 ./av2.pipe b:3196003 ./av3.pipe b:3196662 ./av4.pipe b:3197586 ./av5.pipe > ./finalav.pipe &

tscbrmuxer b:500000 ./oc1.pipe b:100000 ./ewsfinal.pipe b:9195338 ./av1.pipe >./finalav.pipe  &

# Isi dengan NULL file TS yang ada
tsnullfiller ./finalav.pipe 9795338 106581157 > ./finalavnull.pipe &

tsnullshaper ./finalavnull.pipe t:2000 ./ait0.pipe t:2000 ./ewspmt.pipe t:2000 ./pat.pipe t:2000 ./pmt0.pipe t:2000 ./pmt1.pipe t:2000 ./pmt2.pipe t:2000 ./pmt3.pipe t:2000 ./pmt4.pipe t:2000 ./pat.pipe t:2000 ./nit.pipe t:500 ./sdt.pipe t:1000 ./tdt.pipe > ./final.pipe &

tstdt ./final.pipe > ./finaltdt.pipe &

./DtPlay ./finaltdt.pipe -r 30160000 -t 110 -mt OFDM -mC QAM64 -mc 5/6 -mT 2k -mG 1/32 -mf 538.000 &
#./DtPlay ./finaltdt.pipe -t 110 -mt DVBT -mC QAM64 -mc 5/6 -mT 2k -mG 1/32 -mf 538.000 &
#tsloop ./finaltdt.pipe > ./ind-ews-sample..ts &

#tspcrrestamp ./finaltdt.pipe 30160000 > ./finalstamp.pipe &
#tsloop ./finalstamp.pipe > ./test.ts &
#tsloop ./finaltdt.pipe > ./test.ts &
#tsstamp ./finaltdt.pipe 30160000 > ./finalstamp.pipe &
#tsloop ./finalstamp.pipe > ./test.ts &
#tstdt ./final.pipe > ./finaltdt.pipe &
#tsstamp ./finaltdt.pipe 30160000 > ./finalstamp,pipe &
#tsloop ./finalstamp.pipe > ./test.ts &
#tsloop ./final.pipe > ./test.ts &
#tsloop ./final.pipe > ./test.ts &
#tscbrmuxer b:3137798 ./av1.pipe b:3138633 ./av2.pipe b:3140676 ./av3.pipe b:3138121 ./av4.pipe b:3139578 ./av5.pipe b:2200561 ./av6.pipe b:3008 ./pmt0.pipe b:3008 ./pmt1.pipe b:3008 ./pmt2.pipe b:3008 ./pmt3.pipe b:3008 ./pmt4.pipe b:3008 ./pmt5.pipe b:3008 ./pat.pipe b:1500 ./sdt.pipe b:1400 ./nit.pipe b:11932811 ./nullts.pipe > ./final.pipe &
#tstdt ./final.pipe > ./tstdt.pipe &
#tsstamp ./tstdt.pipe 30160000 > ./test.ts &
#tsloop ./final.pipe > ./test.ts &
#tscbrmuxer b:3195568 ./av1.pipe b:3195338 ./av2.pipe b:3196003 ./av3.pipe b:3196662 ./av4.pipe b:3197586 ./av5.pipe b:2227117 ./av6.pipe b:3008 ./pmt.pipe b:3008 ./pat.pipe b:1500 ./sdt.pipe b:1400 ./nit.pipe > ./test.ts &
#./DtPlay ./iucdemo.ts -t 115 -r 22100000 -mf 674.000 -mt QAM64 -l 0 -i 2
#./DtPlay ./iucdemo.ts -t 115 -r 22100000 -mf 674.0 -mt QAM64 -l 0 -i 2
#./DtPlay ./fifofinalall.pipe -t 115 -r 22100000 -mf 674.0 -mt QAM64 -l 0 -i 2 &
