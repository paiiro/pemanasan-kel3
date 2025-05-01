import streamlit as st
import time
import random

# --- Data Bahan Makanan ---
data_makanan = {
    "🥚 Telur": {
        "reaksi": [
            (30, "Telur mulai memanas."),
            (62, "Putih telur menggumpal (albumin denaturasi)."),
            (70, "Kuning telur mengeras (lipovitellenin denaturasi)."),
        ],
        "penjelasan": "Protein seperti albumin dan lipovitellenin pada telur mengalami denaturasi saat dipanaskan.",
        "fun_fact": "Memasak telur perlahan menghasilkan tekstur creamy sempurna!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "3-5 minggu",
            "tips": "Simpan di karton asli, jangan di pintu kulkas."
        }
    },
    "🍬 Gula": {
        "reaksi": [
            (100, "Gula mulai meleleh."),
            (160, "Gula mengalami karamelisasi."),
            (180, "Gula terbakar dan terasa pahit."),
        ],
        "penjelasan": "Karamelisasi mengubah molekul sukrosa menjadi senyawa aromatik berwarna coklat.",
        "fun_fact": "Karamelisasi mulai sekitar 160°C menghasilkan rasa toffee!",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "18-24 bulan",
            "tips": "Simpan di wadah kedap udara."
        }
    },
    "🥩 Daging Sapi": {
        "reaksi": [
            (65, "Protein mulai denaturasi."),
            (150, "Reaksi Maillard memperkaya rasa dan warna."),
        ],
        "penjelasan": "Pemanasan daging menyebabkan denaturasi protein dan Reaksi Maillard, menghasilkan aroma khas.",
        "fun_fact": "Reaksi Maillard adalah kunci kelezatan steak!",
        "penyimpanan": {
            "suhu": "-1 hingga 1°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan dalam pembungkus vakum untuk daya tahan maksimal."
        }
    },
    "🍞 Roti": {
        "reaksi": [
            (100, "Air menguap dari adonan."),
            (120, "Reaksi Maillard membentuk kerak coklat."),
        ],
        "penjelasan": "Panas menyebabkan air menguap dan reaksi Maillard membentuk aroma dan warna roti.",
        "fun_fact": "Warna keemasan roti dari Maillard, bukan karamelisasi!",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "3-7 hari",
            "tips": "Simpan di wadah kedap udara untuk menghindari jamur."
        }
    },
    "🥛 Susu": {
        "reaksi": [
            (85, "Protein kasein menggumpal."),
            (100, "Air dalam susu mulai menguap."),
        ],
        "penjelasan": "Pemanasan menyebabkan protein susu seperti kasein menggumpal, membentuk lapisan film.",
        "fun_fact": "Susu cepat mendidih karena kandungan air yang tinggi!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "5-7 hari setelah dibuka",
            "tips": "Simpan selalu dalam suhu dingin dan tutup rapat."
        }
    },
    "🥔 Kentang": {
        "reaksi": [
            (65, "Pati gelatinisasi, membuat kentang empuk."),
            (160, "Gula dalam kentang mulai karamelisasi saat digoreng."),
        ],
        "penjelasan": "Gelatinisasi pati membuat kentang menjadi empuk saat dimasak.",
        "fun_fact": "Kentang rebus teksturnya berubah di sekitar 65°C!",
        "penyimpanan": {
            "suhu": "7-10°C",
            "masa_simpan": "2-3 bulan",
            "tips": "Jangan simpan di kulkas agar tidak jadi manis berlebihan."
        }
    },
    "🥕 Wortel": {
        "reaksi": [
            (70, "Seluler pecah, membuat wortel lebih empuk."),
            (100, "Gula alami mulai karamelisasi ringan."),
        ],
        "penjelasan": "Panas menghancurkan struktur sel wortel, membuatnya lembut.",
        "fun_fact": "Wortel bisa terasa lebih manis setelah dimasak!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "2-4 minggu",
            "tips": "Simpan dalam plastik berlubang di kulkas."
        }
    },
    "🍗 Ayam": {
        "reaksi": [
            (60, "Protein mulai denaturasi."),
            (75, "Daging ayam matang sempurna, aman dikonsumsi."),
        ],
        "penjelasan": "Protein pada ayam mengalami denaturasi, mengubah tekstur menjadi padat.",
        "fun_fact": "Suhu ideal untuk ayam juicy adalah 75°C!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "1-2 hari",
            "tips": "Masak segera setelah membeli atau bekukan."
        }
    },
    "🌽 Jagung": {
        "reaksi": [
            (65, "Pati gelatinisasi, membuat biji jagung empuk."),
            (100, "Air menguap, biji jagung bisa meletup (popcorn)."),
        ],
        "penjelasan": "Panas memecah dinding sel biji jagung, menghasilkan tekstur empuk.",
        "fun_fact": "Popcorn terjadi karena uap air meledakkan biji jagung!",
        "penyimpanan": {
            "suhu": "10-15°C",
            "masa_simpan": "6-12 bulan (kering)",
            "tips": "Simpan dalam tempat kering dan kedap udara."
        }
    },
    "🍅 Tomat": {
        "reaksi": [
            (70, "Pelembutan dinding sel."),
            (90, "Air menguap, meningkatkan konsentrasi rasa."),
        ],
        "penjelasan": "Pemanasan melunakkan struktur sel tomat, memperkuat rasa alami.",
        "fun_fact": "Tomat yang dipanaskan terasa lebih umami!",
        "penyimpanan": {
            "suhu": "12-15°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan pada suhu ruangan untuk rasa terbaik."
        }
    },
    "🍚 Beras": {
        "reaksi": [
            (65, "Pati mulai gelatinisasi."),
            (100, "Air terserap, beras menjadi pulen."),
        ],
        "penjelasan": "Pati dalam beras gelatinisasi dengan air panas, mengubah tekstur menjadi lembut.",
        "fun_fact": "Rahasia nasi pulen adalah gelatinisasi sempurna pada 65-75°C!",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "6-12 bulan (kering)",
            "tips": "Simpan di tempat kering dan sejuk."
        }
    },
    "🍆 Terong": {
        "reaksi": [
            (80, "Sel dinding pecah, membuat terong empuk."),
            (100, "Air menguap, tekstur semakin lembut."),
        ],
        "penjelasan": "Terong menjadi sangat lembut saat struktur selnya pecah karena panas.",
        "fun_fact": "Terong menyerap banyak minyak saat digoreng!",
        "penyimpanan": {
            "suhu": "10-12°C",
            "masa_simpan": "4-7 hari",
            "tips": "Simpan dalam suhu agak dingin, bukan kulkas ekstrem."
        }
    },
    "🧅 Bawang": {
        "reaksi": [
            (85, "Enzim sulfur terurai, rasa bawang menjadi manis."),
            (100, "Karamelisasi dimulai, rasa kompleks muncul."),
        ],
        "penjelasan": "Pemanasan memecah senyawa sulfur dalam bawang, membuat rasa manis dan lembut.",
        "fun_fact": "Memasak bawang perlahan menghasilkan rasa karamel alami!",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "1-2 bulan",
            "tips": "Simpan di tempat sejuk, gelap, dan berventilasi."
        }
    },
    "🥒 Mentimun": {
        "reaksi": [
            (60, "Sel mulai pecah, tekstur melembek."),
        ],
        "penjelasan": "Mentimun cepat kehilangan kerenyahannya saat dipanaskan.",
        "fun_fact": "Mentimun lebih nikmat disajikan segar daripada dimasak!",
        "penyimpanan": {
            "suhu": "10-12°C",
            "masa_simpan": "1 minggu",
            "tips": "Jauhkan dari suhu sangat dingin untuk mencegah lecet."
        }
    },
    "🧀 Keju": {
        "reaksi": [
            (30, "Keju mulai melunak."),
            (60, "Lemak dalam keju mulai meleleh."),
            (90, "Protein koagulasi, membentuk lapisan kering."),
        ],
        "penjelasan": "Pemanasan keju menyebabkan lemak meleleh dan protein bergumpal membentuk kerak lezat.",
        "fun_fact": "Keju mozzarella meleleh paling sempurna di 60°C!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "1-2 minggu setelah dibuka",
            "tips": "Bungkus keju dengan kertas lilin lalu plastik."
        }
    },
}


# --- Fungsi ---
def get_multi_reaksi(makanan, suhu):
    reaksi_list = []
    for batas_suhu, reaksi in data_makanan[makanan]["reaksi"]:
        if suhu >= batas_suhu:
            reaksi_list.append(f"- {batas_suhu}°C: {reaksi}")
    if not reaksi_list:
        return ["Belum ada perubahan signifikan."]
    return reaksi_list

# --- Streamlit App ---
st.set_page_config(page_title="Simulasi Pemanasan Pada Pangan", page_icon="🍽️", layout="centered")
st.title("🍽️ Simulasi Pemanasan Pada Pangan")

# Pilih Mode
mode = st.radio("🎭 Simulasi Sebagai:", ("Chef", "Analis"))

# Pilih Makanan
makanan = st.selectbox("🔍 Pilih Bahan Makanan:", list(data_makanan.keys()))
pilihan_simulasi = st.radio("🔥 Mau set suhu manual atau simulasi pemanasan?", ("Set Suhu Manual", "Simulasi Pemanasan"))

if pilihan_simulasi == "Set Suhu Manual":
    suhu = st.slider("🌡️ Atur Suhu (°C):", 0, 300, 25)
else:
    suhu = 0
    progress = st.progress(0)
    for i in range(301):
        suhu = i
        progress.progress(i / 300)
        time.sleep(0.005)
    st.success("Simulasi selesai!")

# Tampilkan reaksi
st.subheader(f"🔥 Pada suhu {suhu}°C:")
reaksi_multi = get_multi_reaksi(makanan, suhu)
for r in reaksi_multi:
    if mode == "Chef Mode":
        if any(k in r.lower() for k in ["karamelisasi", "garing", "renyah", "meleleh", "harum"]):
            st.success(r)
        elif "melunak" in r.lower() or "mengering" in r.lower():
            st.warning(r)
        else:
            st.info(r)
    else:  # Science Mode
        if any(k in r.lower() for k in ["denaturasi", "karamelisasi", "maillard"]):
            st.success(r)
        elif "pecah" in r.lower() or "menggumpal" in r.lower():
            st.warning(r)
        else:
            st.info(r)

# Efek suhu umum
if suhu >= 150:
    st.markdown("<h3 style='color:red;'>⚡ Reaksi besar terjadi! ⚡</h3>", unsafe_allow_html=True)
elif suhu >= 100:
    st.markdown("<h4 style='color:orange;'>🔥 Memasak aktif! Aroma khas muncul! 🔥</h4>", unsafe_allow_html=True)
elif suhu >= 50:
    st.markdown("<h5 style='color:green;'>🌡️ Reaksi awal mulai! 🌡️</h5>", unsafe_allow_html=True)
else:
    st.markdown("<h5 style='color:gray;'>❄️ Belum ada reaksi signifikan. ❄️</h5>", unsafe_allow_html=True)

# Divider
st.divider()

# Penjelasan tambahan
if mode == "Chef Mode":
    st.subheader("🍳 Tips & Fun Fact untuk Chef:")
    st.info(f"💡 {data_makanan[makanan]['fun_fact']}")
else:
    st.subheader("🔬 Penjelasan Kimia Lanjut:")
    st.write(data_makanan[makanan]["penjelasan"])

# Divider
st.divider()

# Penyimpanan
st.subheader("🧊 Cara Penyimpanan:")
penyimpanan = data_makanan[makanan]["penyimpanan"]
st.write(f"• **Suhu Penyimpanan:** {penyimpanan['suhu']}")
st.write(f"• **Masa Simpan:** {penyimpanan['masa_simpan']}")
st.write(f"• **Tips:** {penyimpanan['tips']}")

# Footer
st.caption("🎯 Simulasi by Kelompok 3 PMIP 1E-2")
