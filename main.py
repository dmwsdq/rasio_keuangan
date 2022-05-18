from telnetlib import STATUS
from click import option
import streamlit as st
import math

def id_fmt(val):
    string_temp = "{:,.2f}".format(val)
    char_to_replace = {',': '.','.': ','}
    return string_temp.translate(str.maketrans(char_to_replace))

def int_fmt(val):
    string_temp = "{:,}".format(val)
    char_to_replace = {',': '.','.': ','}
    return string_temp.translate(str.maketrans(char_to_replace))

st.title("Aplikasi Ratio Keuangan")
option = st.sidebar.selectbox ('Silahkan di pilih :',['Home', 'profitMargin', 'breakEven','salesGrowth', 'burnRate'])

if option == 'Home' or option == '': #Halaman Utama
    st.subheader ("Home")
    st.write('''
        Setiap Wirausahawan perlu mengetahui Rasio keuangan yang bisa membantu mereka dalam mengelola bisnis.
        Aplikasi ini akan membantu anda menghitung dan menjelaskan rasio keuangan berikut untuk mengelola bisnis Anda agar semakin maju.
    ''')
    status = st.radio ("Apa yang ingin Anda Ketahui : ",('Burn_Rate','Sales_Growth', 'Profit_Margin', 'Break_Even'))
    if (status == 'Profit_Margin') :
        st.subheader("Profit Margin (Margin Keuntungan)")
        st.write('''
            Profit Margin (Margin Keuntungan) adalah seberapa banyak penjualan kotor anda yang dikonversi menjadi keuntungan.
            Dengan kata lain, ini adalah besarnya keuntungan yang Anda dapat dari tiap 1 Rupiah penjualan kotor Anda.
        ''')
        st.text("Rumus Perhitungan :")
        st.code('''

            profit_margin =  (penjualan_kotor - total_biaya_usaha ) / penjualan_kotor

        ''')
        st.write("Contoh Simulasi :")
        pk = st.number_input('Penjualan Kotor (Rupiah)') #input data penjualan kotor
        bu = st.number_input('Total Biaya Usaha (Rupiah)') #input data total biaya usaha

        if (not pk) or (not bu) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

        if st.button('Hitung Profit Margin') : #
            try:
                hasilProfit = (pk-bu)/pk
                st.success ("Profit Margin Anda adalah "+id_fmt(hasilProfit*100)+"%")
                st.info("Dari setiap 1 rupiah penjualan kotor Anda, anda mendapatkan keuntungan sebesar "+id_fmt(hasilProfit) + 
                " rupiah. Dengan kata lain, jika Anda berhasil mendapat total penjualan kotor sebesar Rp100.000, keuntungan anda adalah Rp"+id_fmt(hasilProfit*100000)+ 
                ". Jika Anda merasa keuntungannya terlalu sedikit, anda harus meningkatkan penjualan Anda atau menurunkan biaya usaha Anda.")
            except ZeroDivisionError :
                st.error ('Sorry, ada yang salah dalam sistem')
    elif (status == 'Break_Even') :
        st.subheader("Break Even (Titik Impas) ")
        st.write('''
            Breakeven (titik impas) adalah jumlah barang/jasa yang harus Anda Jual sebelum Anda bisa mendapatkan keuntungan
        ''')
        st.text("Rumus Perhitungan :")
        st.code('''

            breakeven =  {Total_biaya_per_hari} / {harga_barang_per_satuan}

        ''')
        st.write("Contoh Simulasi :")
        tb = st.number_input('Total Biaya Per Hari (Rupiah)') #input data 
        hb = st.number_input('Harga Barang Per Satuan (Rupiah)') #input data

        if (not tb) or (not hb) :
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

        if st.button('Hitung Break Even') :
            try:
                hasilBreak = int (math.ceil( tb / hb))
                st.success ("Break Even Anda adalah "+int_fmt(hasilBreak))
                st.info("Jumlah Barang yang harus anda jual tiap hari sebelum anda bisa untung adalah "+int_fmt(hasilBreak)+" buah. Jika Anda Sulit mencapai jumlah itu, anda harus menaikkan harga barang atau menurunkan biaya usaha supaya bisa untung")
            except ZeroDivisionError :
                st.error ('Sorry, ada yang salah dalam sistem')    
    elif (status == 'Sales_Growth') :
        st.subheader("Sales Growth (Pertumbuhan Penjualan)")
        st.write('''
            Pertumbuhan Penjualan adalah Rasio yang paling tepat untuk mengukur pertumbuhan usaha Anda.
            Pertumbuhan Penjualan bisa dihitung per minggu, per bulan, per tahun, atau sesuai kebutuhan Anda.
        ''')
        st.text("Rumus Perhitungan :")
        st.code('''

            Sales Growth =  ((Penjualan_periode_ini - Penjualan_periode_sebelumnya) x 100) / Penjualan_periode_sebelumnya

        ''')
        st.write("Contoh Simulasi :")
        pps = st.number_input('Penjualan pada Periode Sebelumnya (Rupiah)') #input data penjualan periode sebelumnya
        ppi = st.number_input('Penjualan pada Periode Ini (Rupiah)') #input data penjualan periode ini

        if (not pps) or (not ppi) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

        if st.button('Hitung Sales Growth') : #
            try:
                hasilSales = ((ppi-pps)*100)/pps
                st.success ("Sales Growth Anda adalah {:.2f}".format(hasilSales) + "%")
                st.info("Pertumbuhan Penjualan Anda adalah {:.2f}".format(hasilSales) + "%." 
                " Dengan kata lain, penjualan Anda Naik {:.2f}".format(hasilSales) + "%." + "dari periode sebelumnya." +
                " Jika Anda merasa pertumbuhannya terlalu kecil, Anda Harus meningkatkan Penjualan Anda." )
            except ZeroDivisionError :
                st.error ('Sorry, ada yang salah dalam sistem')
    else :
        st.subheader("Burn Rate (Tingkat Pembakaran)")
        st.write('''
            Tingkat Pembakaran adalah jumlah uang yang Anda habiskan di usaha Anda selama jangka waktu tertentu.
        ''')
        st.text("Rumus Perhitungan :")
        st.code('''

            Burn Rate =  (Uang_Awal_Tahun - Uang_Akhir_Tahun) / 12

        ''')
        st.write("Contoh Simulasi :")
        uat = st.number_input('Uang Modal Usaha di Akhir Tahun (Rupiah)') #input data Uang Akhir Tahun
        uwt = st.number_input('Uang Modal Usaha di Awal Tahun (Rupiah)') #input data Uang Awal Tahun

        if (not uat) or (not uwt) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

        if st.button('Hitung Burn Rate') : #
            try:
                hasilBurn = (uwt-uat)/12
                st.success ("Burn Rate Anda adalah {:.2f}".format(hasilBurn) + "/bulan")
                st.info("Tingkat Pembakaran Anda adalah Rp {:.2f}".format(hasilBurn) + "/bulan" +
                "Dengan kata lain, tiap bulan Anda menghabiskan Uang untuk usaha Anda sebanyak Rp {:.2f}".format(hasilBurn) + 
                "Jika Anda merasa tingkat pembakarannya terlalu besar, Anda harus menekan Biaya Usaha Anda.")
            except ZeroDivisionError :
                st.error ('Sorry, ada yang salah dalam sistem')

elif option == 'profitMargin' : #Profit Margin
    st.subheader("Profit Margin (Margin Keuntungan)")
    st.write('''
        Profit Margin (Margin Keuntungan) adalah seberapa banyak penjualan kotor anda yang dikonversi menjadi keuntungan.
        Dengan kata lain, ini adalah besarnya keuntungan yang Anda dapat dari tiap 1 Rupiah penjualan kotor Anda.
    ''')
    st.text("Rumus Perhitungan :")
    st.code('''

        profit_margin =  (penjualan_kotor - total_biaya_usaha ) / penjualan_kotor

        ''')
    st.write("Contoh Simulasi :")
    pk = st.number_input('Penjualan Kotor (Rupiah)') #input data penjualan kotor
    bu = st.number_input('Total Biaya Usaha (Rupiah)') #input data total biaya usaha

    if (not pk) or (not bu) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

    if st.button('Hitung Profit Margin') : #
        try:
            hasilProfit = (pk-bu)/pk
            st.success ("Profit Margin Anda adalah "+id_fmt(hasilProfit*100)+"%")
            st.info("Dari setiap 1 rupiah penjualan kotor Anda, anda mendapatkan keuntungan sebesar "+id_fmt(hasilProfit) + 
                " rupiah. Dengan kata lain, jika Anda berhasil mendapat total penjualan kotor sebesar Rp100.000, keuntungan anda adalah Rp"+id_fmt(hasilProfit*100000)+ 
                ". Jika Anda merasa keuntungannya terlalu sedikit, anda harus meningkatkan penjualan Anda atau menurunkan biaya usaha Anda.")
        except ZeroDivisionError :
            st.error ('Sorry, ada yang salah dalam sistem')

elif option == 'breakEven': #Break Even
    st.subheader("Break Even (Titik Impas) ")
    st.write('''
        Breakeven (titik impas) adalah jumlah barang/jasa yang harus Anda Jual sebelum Anda bisa mendapatkan keuntungan
    ''')
    st.text("Rumus Perhitungan :")
    st.code('''

        breakeven =  {Total_biaya_per_hari} / {harga_barang_per_satuan}

        ''')
    st.write("Contoh Simulasi :")
    tb = st.number_input('Total Biaya Per Hari (Rupiah)') #input data 
    hb = st.number_input('Harga Barang Per Satuan (Rupiah)') #input data

    if (not tb) or (not hb) :
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

    if st.button('Hitung Break Even') :
        try:
            hasilBreak = int(math.ceil( tb / hb))
            st.success ("Break Even Anda adalah "+int_fmt(hasilBreak))
            st.info("Jumlah Barang yang harus anda jual tiap hari sebelum anda bisa untung adalah "+int_fmt(hasilBreak)+" buah. Jika Anda Sulit mencapai jumlah itu, anda harus menaikkan harga barang atau menurunkan biaya usaha supaya bisa untung")
        except ZeroDivisionError :
            st.error ('Sorry, ada yang salah dalam sistem') 

elif option == 'salesGrowth' : #Sales Growth
    st.subheader("Sales Growth (Pertumbuhan Penjualan)")
    st.write('''
       Pertumbuhan Penjualan adalah Rasio yang paling tepat untuk mengukur pertumbuhan usaha Anda.
       Pertumbuhan Penjualan bisa dihitung per minggu, per bulan, per tahun, atau sesuai kebutuhan Anda.
    ''')
    st.text("Rumus Perhitungan :")
    st.code('''

        Sales Growth =  ((Penjualan_periode_ini - Penjualan_periode_sebelumnya) x 100 ) / Penjualan_periode_sebelumnya

        ''')
    st.write("Contoh Simulasi :")
    pps = st.number_input('Penjualan pada Periode Sebelumnya (Rupiah)') #input data penjualan periode sebelumnya
    ppi = st.number_input('Penjualan pada Periode Ini (Rupiah)') #input data penjualan periode ini

    if (not pps) or (not ppi) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

    if st.button('Hitung Sales Growth') : #
        try:
            hasilSales = ((ppi-pps)*100)/pps
            st.success ("Sales Growth Anda adalah {:.2f}".format(hasilSales) + "%")
            st.info("Pertumbuhan Penjualan Anda adalah {:.2f}".format(hasilSales) + "%." 
            " Dengan kata lain, penjualan Anda Naik {:.2f}".format(hasilSales) + "%." + "dari periode sebelumnya." +
            " Jika Anda merasa pertumbuhannya terlalu kecil, Anda Harus meningkatkan Penjualan Anda." )
        except ZeroDivisionError :
            st.error ('Sorry, ada yang salah dalam sistem')

elif option == 'burnRate' : #Burn Rate
    st.subheader("Burn Rate (Tingkat Pembakaran)")
    st.write('''
        Tingkat Pembakaran adalah jumlah uang yang Anda habiskan di usaha Anda selama jangka waktu tertentu.
    ''')
    st.text("Rumus Perhitungan :")
    st.code('''

        Burn Rate =  (Uang_Awal_Tahun - Uang_Akhir_Tahun) / 12

        ''')
    st.write("Contoh Simulasi :")
    uat = st.number_input('Uang Modal Usaha di Akhir Tahun (Rupiah)') #input data Uang Akhir Tahun
    uwt = st.number_input('Uang Modal Usaha di Awal Tahun (Rupiah)') #input data Uang Awal Tahun

    if (not uat) or (not uwt) : #apabila salah satu belum ada nilai, tidak akan diproses
            st.warning('Anda Belum Memasukkan Nilai')
            st.stop()

    if st.button('Hitung Burn Rate') : #
        try:
            hasilBurn = (uwt-uat)/12
            st.success ("Burn Rate Anda adalah {:.2f}".format(hasilBurn) + "/bulan")
            st.info("Tingkat Pembakaran Anda adalah Rp {:.2f}".format(hasilBurn) + "/bulan" +
            "Dengan kata lain, tiap bulan Anda menghabiskan Uang untuk usaha Anda sebanyak Rp {:.2f}".format(hasilBurn) + 
            "Jika Anda merasa tingkat pembakarannya terlalu besar, Anda harus menekan Biaya Usaha Anda.")
        except ZeroDivisionError :
            st.error ('Sorry, ada yang salah dalam sistem')

