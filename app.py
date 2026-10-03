import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("💰 TÍNH LÃI TIỀN GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính số tiền lãi nhận được.")

st.divider()

# ==============================
# NHẬP DỮ LIỆU
# ==============================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH TIỀN LÃI", use_container_width=True):

    # Kiểm tra dữ liệu
    if tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    elif lai_suat < 0:
        st.error("Lãi suất không được nhỏ hơn 0.")
    else:

        # --------------------------------
        # TÍNH TỔNG TIỀN LÃI
        # Công thức:
        # Lãi = Gốc × Lãi suất năm × Số tháng / 12
        # --------------------------------

        tong_lai = tien_gui * (lai_suat / 100) * (ky_han / 12)

        # --------------------------------
        # XÁC ĐỊNH TIỀN LÃI ĐỊNH KỲ
        # --------------------------------

        if hinh_thuc == "Cuối kỳ":

            so_ky = 1
            lai_dinh_ky = tong_lai
            ten_ky = "cuối kỳ"

        elif hinh_thuc == "Hàng tháng":

            so_ky = ky_han
            lai_dinh_ky = tong_lai / so_ky
            ten_ky = "tháng"

        else:  # Hàng quý

            so_ky = ky_han / 3

            # Nếu kỳ hạn không chia hết cho 3,
            # vẫn tính tiền lãi bình quân theo quý.
            lai_dinh_ky = tong_lai / so_ky
            ten_ky = "quý"

        # Tổng số tiền cuối cùng
        tong_tien = tien_gui + tong_lai

        # ==============================
        # HIỂN THỊ KẾT QUẢ
        # ==============================

        st.success("✅ TÍNH TOÁN THÀNH CÔNG")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💰 Tiền lãi định kỳ",
                f"{lai_dinh_ky:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "📈 Tổng tiền lãi",
                f"{tong_lai:,.0f} VNĐ"
            )

        st.metric(
            "💵 Tổng tiền gốc + lãi",
            f"{tong_tien:,.0f} VNĐ"
        )

        st.divider()

        # ==============================
        # THÔNG TIN CHI TIẾT
        # ==============================

        st.subheader("📋 Chi tiết khoản tiền gửi")

        st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

        if hinh_thuc == "Cuối kỳ":
            st.info(
                f"Bạn nhận toàn bộ tiền lãi {lai_dinh_ky:,.0f} VNĐ vào cuối kỳ."
            )

        elif hinh_thuc == "Hàng tháng":
            st.info(
                f"Bạn nhận khoảng {lai_dinh_ky:,.0f} VNĐ tiền lãi mỗi tháng."
            )

        else:
            st.info(
                f"Bạn nhận khoảng {lai_dinh_ky:,.0f} VNĐ tiền lãi mỗi quý."
            )

# ==============================
# GHI CHÚ
# ==============================

st.divider()

st.caption(
    "📌 Lưu ý: Kết quả được tính theo lãi suất đơn, "
    "chưa xét thuế, phí hoặc các chính sách riêng của từng ngân hàng."
)
