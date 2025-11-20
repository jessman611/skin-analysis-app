import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

# --- 頁面設定 ---
st.set_page_config(page_title="AI 醫美極致美白檢測系統", layout="wide")

# --- 側邊欄：顧客資料 ---
with st.sidebar:
    st.title("MED-AI 診療控制台")
    st.markdown("---")
    st.subheader("顧客檔案")
    name = st.text_input("顧客姓名", "Guest")
    skin_type = st.selectbox("膚質", ["乾性", "油性", "混合性", "敏感性"])
    history = st.multiselect("過往病史/特徵", ["黃褐斑 (Melasma)", "曬斑", "PIH (發炎後色素)", "敏感肌"])

    st.markdown("---")
    st.success("✅ 設備參數已載入：\n- Whitening Chamber (550-680nm)\n- Laser / IPL\n- Chemical Peels")

# --- 主標題 ---
st.title("🧬 智能光學皮膚分析與療程規劃系統")
st.markdown(f"Expert Analysis for: **{name}** | Skin Type: **{skin_type}**")

# --- 圖片上傳 ---
col1, col2 = st.columns(2)
with col1:
    img_file = st.file_uploader("📸 上傳檢測影像", type=["jpg", "png"])
    if img_file:
        st.image(Image.open(img_file), use_container_width=True)

# --- 分析按鈕 ---
if st.button("🚀 開始 AI 分析與療程配對", type="primary"):
    if not img_file:
        st.error("請上傳照片")
    else:
        # 模擬 AI 運算過程
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("正在掃描表皮層黑色素分佈 (Scanning Melanin Caps)...")
        time.sleep(0.5)
        progress_bar.progress(30)

        status_text.text("正在評估真皮層血管擴張與 ET-1 活躍度...")
        time.sleep(0.5)
        progress_bar.progress(60)

        status_text.text("正在計算 MITF 抑制需求與最佳療程頻率...")
        time.sleep(0.5)
        progress_bar.progress(100)
        time.sleep(0.2)
        status_text.empty()
        progress_bar.empty()

        # ============================================
        # 模擬分析結果 (未來可接 LLM API)
        # ============================================

        # 假設檢測數值 (0-100, 越高越嚴重)
        scores = {
            "surface_spots": 75,  # 適合 Laser
            "redness": 60,  # 適合 IPL/美白倉紅光
            "deep_melanin": 85,  # 適合 美白倉綠光
            "dullness": 40  # 適合 煥膚
        }

        st.markdown("### 📊 1. 皮膚生理檢測數據")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🐆 表層斑點", f"{scores['surface_spots']}/100", "需物理性擊碎")
        c2.metric("🔴 發炎紅區", f"{scores['redness']}/100", "微血管擴張")
        c3.metric("🌑 深層黑色素", f"{scores['deep_melanin']}/100", "MITF 高度活躍", delta_color="inverse")
        c4.metric("✨ 角質堆積", f"{scores['dullness']}/100", "代謝稍慢")

        st.markdown("---")

        # --- 療程推薦邏輯 (基於文獻) ---
        st.markdown("### 👩‍⚕️ 2. AI 醫學療程處方 (Treatment Protocol)")

        tab1, tab2, tab3 = st.tabs(["💡 光電雷射規劃", "💊 煥膚與修復", "📅 建議頻率表"])

        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                st.subheader("全身美白倉 (550-680nm)")
                st.info("**推薦重點：抑制源頭 + 抗炎修復**")
                st.markdown(f"""
                * **機制**：利用 **550nm** 波段抑制 **MITF** 轉錄因子，減少黑色素生成 [cite: 2281]。同時利用 **600-680nm** 波段降低 PGE2 發炎因子 。
                * **針對問題**：您的深層黑色素指數高達 {scores['deep_melanin']}，這是最適合的非侵入式療程。
                * **安全性**：根據 *Mima et al. (2025)*，每日照射對細胞存活率無影響 [cite: 2341]，適合高頻率保養。
                """)

            with col_b:
                st.subheader("Laser / IPL 聯合治療")
                st.warning("**推薦重點：擊碎現有斑點**")
                st.markdown("""
                * **機制**：針對表皮層已形成的 **Supranuclear Melanin Cap** (微遮陽傘結構) 進行熱破壞 。IPL 可同時封閉擴張血管，阻斷 ET-1 供給 [cite: 1961]。
                * **針對問題**：表層斑點 ({scores['surface_spots']}) 與 紅區 ({scores['redness']})。
                """)

        with tab2:
            st.subheader("化學酸類煥膚 (Chemical Peels)")
            st.markdown("""
            * **機制**：促進表皮更新 (Turnover)，加速含有黑色素的角質細胞脫落。
            * **文獻支持**：*Serre et al. (2018)* 指出，促進 **Autophagy (自噬作用)** 是降解黑色素小體的關鍵路徑 [cite: 506]。
            * **協同效應**：煥膚後皮膚對光療的穿透率會提升。
            """)

        with tab3:
            st.subheader("🗓️ 整合治療時間軸 (8週計畫)")

            # 建立一個簡單的 Pandas 表格來顯示頻率
            schedule_data = {
                "療程項目": ["全身美白倉 (550-680nm)", "皮秒/淨膚雷射", "IPL 脈衝光", "化學煥膚"],
                "建議頻率": ["每週 2 次", "每 4 週 1 次", "每 3-4 週 1 次", "每 2-3 週 1 次"],
                "原理依據": [
                    "抑制 MITF/Tyrosinase (需持續累積能量) [cite: 2281]",
                    "破壞黑色素小體 (需修復期) ",
                    "收縮血管/抗炎 [cite: 1961]",
                    "加速角質代謝 [cite: 502]"
                ],
                "本週建議": ["✅ 立即執行", "⚠️ 需敷麻藥", "❌ 與雷射間隔1週", "❌ 與雷射錯開"]
            }
            df_schedule = pd.DataFrame(schedule_data)
            st.table(df_schedule)

            st.caption("*註：引用文獻來自 J. Dermatol (2025), Int J Cosm Sci (2018), Pigment Cell Res (2000)*")

        st.markdown("---")

        # --- 預測模擬 ---
        st.markdown("### 🔮 3. 療程效果預測 (Prognosis)")
        c_pred1, c_pred2 = st.columns(2)

        with c_pred1:
            st.error("⚠️ 不處理：變黑風險預測")
            st.markdown("""
            若不進行干預，**UVB 誘導的 c-KIT 與 EDNRB 受體** 將持續高表現 [cite: 3173]，導致黑色素細胞對刺激更加敏感。預計 1 年後斑點加深 **20-30%**。
            """)

        with c_pred2:
            st.success("✨ 完整療程後：美白極限")
            st.markdown("""
            根據 *Mima et al. (2025)* 人體實驗數據，使用 LED 光療 8 週後，**Melanin Index** 顯著下降 [cite: 2822]，且皮膚亮度 ($L^*$ value) 提升。預計可還原至您手臂內側的原始膚色。
            """)
