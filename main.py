import streamlit as st
import math

st.title('Rasio Keuangan')
st.write('Setiap wirausahawan perlu mengetahui rasio keuangan yang bisa membantu mereka dalam mengelola bisnis. Aplikasi ini akan membantu anda menghitung dan menjelaskan rasio keuangan berikut untuk mengelola bisnis anda agar semakin maju:')

with st.expander("Breakeven"):
    st.write('Breakeven (titik impas) adalah jumlah barang/jasa yang harus Anda jual sebelum Anda bisa mendapatkan keuntungan.')
    total_biaya_per_hari = st.number_input('Total biaya per hari')
    harga_barang_per_satuan = st.number_input('Harga barang per satuan')
    if st.button('Hitung'):
        breakeven = math.ceil(total_biaya_per_hari / harga_barang_per_satuan)
        st.write('Jumlah barang yang harus anda jual tiap hari sebelum anda bisa untung adalah '+str(breakeven)+' buah. Jika anda sulit mencapai jumlah itu, anda harus menaikkan harga barang atau menurunkan biaya usaha supaya bisa untung.')

with st.expander("Profit Margin"):
    st.write('Profit margin (margin keuntungan) adalah seberapa banyak penjualan kotor anda yang dikonversi menjadi keuntungan. Dengan kata lain, ini adalah besarnya keuntungan yang anda dapat dari tiap 1 rupiah penjualan kotor anda. ')
    penjualan_kotor  = st.number_input('Penjualan Kotor')
    total_biaya_usaha = st.number_input('Total Biaya Usaha')
    if st.button('Hitung '):
        profit_margin = round((penjualan_kotor - total_biaya_usaha)/ penjualan_kotor,2)
        st.write('Dari setiap 1 rupiah penjualan kotor anda, anda mendapatkan keuntungan sebesar '+ str(profit_margin) + ' rupiah. Dengan kata lain, jika anda berhasil mendapat total penjualan kotor sebesar Rp100.000, keuntungan anda adalah '+ str(profit_margin*100000) + ' rupiah. Jika anda merasa keuntungannya terlalu sedikit, anda harus meningkatkan penjualan anda atau menurunkan biaya usaha anda.')

with st.expander("Sales Growth"):
    st.write('Pertumbuhan penjualan adalah rasio yang paling tepat untuk mengukur pertumbuhan usaha anda. Pertumbuhan penjualan bisa dihitung per minggu, per bulan, per tahun, atau sesuai kebutuhan anda.')
    penjualan_periode_sebelumnya  = st.number_input('Penjualan Periode Sebelumnya')
    penjualan_periode_ini = st.number_input('Penjualan Periode Ini')
    if st.button('Hitung  '):
        sales_growth = round((penjualan_periode_sebelumnya - penjualan_periode_ini)/ penjualan_periode_sebelumnya,2)*100
        st.write('Pertumbuhan penjualan anda adalah '+ str(sales_growth) + '\%\. Dengan kata lain, penjualan anda naik '+ str(sales_growth) + '\% \dari periode sebelumnya. Jika anda merasa pertumbuhannya terlalu kecil, anda harus meningkatkan penjualan anda.')   

with st.expander("Burn Rate"):
    st.write('Tingkat pembakaran adalah jumlah uang yang anda habiskan di usaha anda selama jangka waktu tertentu.')
    uang_awal_tahun  = st.number_input('Uang untuk Modal Usaha di Awal Tahun')
    uang_akhir_tahun  = st.number_input('Uang untuk Modal Usaha di Akhir Tahun ')
    if st.button('Hitung   '):
        burn_rate = round((uang_akhir_tahun - uang_awal_tahun)/12,2) 
        st.write('Tingkat pembakaran anda adalah Rp'+ str(burn_rate) + '/bulan. Dengan kata lain, tiap bulan anda menghabiskan uang untuk usaha anda sebanyak Rp'+ str(burn_rate)+'. Jika anda merasa tingkat pembakarannya terlalu besar, anda harus menekan biaya usaha anda.')   