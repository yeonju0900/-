def calculate_concentration():
    print("=" * 45)
    print("🧪 퍼센트농도 ↔ 몰농도 변환기")
    print("=" * 45)

    try:
        # 1. 사용자 입력 받기
        percent = float(input("▶ 퍼센트농도(%)를 입력하세요: "))
        mw = float(input("▶ 용질의 화학식량(g/mol)을 입력하세요: "))
        
        # 밀도는 모를 경우 1.0으로 기본 처리
        density_str = input("▶ 용액의 밀도(g/mL)를 입력하세요 (모르면 엔터, 기본값 1.0): ")
        density = float(density_str) if density_str.strip() else 1.0
        
        volume = float(input("▶ 용액의 양(L)을 입력하세요: "))

        # 2. 계산 수행
        # 몰농도(M) = (10 * 밀도 * 퍼센트농도) / 화학식량
        molarity = (10 * density * percent) / mw
        total_moles = molarity * volume

        # 3. 결과 출력
        print("-" * 45)
        print("✅ [계산 결과]")
        print(f" - 용액의 몰농도: {molarity:.4f} M")
        if volume > 0:
            print(f" - 용액 {volume}L 내 총 몰수: {total_moles:.4f} mol")
        print("=" * 45)

    except ValueError:
        print("\n⚠️ 입력 오류: 숫자만 정확하게 입력해 주세요.")
    except ZeroDivisionError:
        print("\n⚠️ 계산 오류: 화학식량은 0이 될 수 없습니다.")

if __name__ == "__main__":
    calculate_concentration()
