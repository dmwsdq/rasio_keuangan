import streamlit as st

st.title('Rasio Keuangan')
st.write('Setiap wirausahawan perlu mengetahui rasio keuangan yang bisa membantu mereka dalam mengelola bisnis. Aplikasi ini akan membantu anda menghitung dan menjelaskan rasio keuangan berikut untuk mengelola bisnis anda agar semakin maju:')


with st.expander("Breakeven"):
    st.write('Breakeven (titik impas) adalah jumlah barang/jasa yang harus Anda jual sebelum Anda bisa mendapatkan keuntungan.')
    total_biaya_per_hari = st.number_input('Total biaya per hari')
    harga_barang_per_satuan = st.number_input('Harga barang per satuan')
    if st.button('Hitung'):
        breakeven = total_biaya_per_hari / harga_barang_per_satuan
        st.write('Jumlah barang yang harus anda jual tiap hari sebelum anda bisa untung adalah'+breakeven+'buah. Jika anda sulit mencapai jumlah itu, anda harus menaikkan harga barang atau menurunkan biaya usaha supaya bisa untung.')

with st.expander("Breakeven"):
    st.write('Breakeven (titik impas) adalah jumlah barang/jasa yang harus Anda jual sebelum Anda bisa mendapatkan keuntungan.')
    total_biaya_per_hari = st.number_input('Total biaya per hari')
    harga_barang_per_satuan = st.number_input('Harga barang per satuan')
    if st.button('Hitung'):
        breakeven = total_biaya_per_hari / harga_barang_per_satuan
        st.write('Jumlah barang yang harus anda jual tiap hari sebelum anda bisa untung adalah'+breakeven+'buah. Jika anda sulit mencapai jumlah itu, anda harus menaikkan harga barang atau menurunkan biaya usaha supaya bisa untung.')