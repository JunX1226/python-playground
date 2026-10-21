# 固定系数
COEF_A = 28.97
COEF_B = 21.72

def main():
    print("=== 总和差值计算器 ===")
    print(f"公式：B = sum - A")
    print(f"结果 = A × {COEF_A} + B × {COEF_B}\n")
    
    while True:
        try:
            # 输入 sum 和 A
            sum_val = float(input("请输入总和 sum: "))
            A = float(input("请输入变量 想·A: "))
            
            # 计算 B
            B = sum_val - A
            
            # 计算结果
            result = A * COEF_A + B * COEF_B
            
            # 输出详细过程
            print("\n------ 计算过程 ------")
            print(f"B = {sum_val} - {A} = {B:.4f}")
            print(f"结果 = {A:.4f} × {COEF_A} + {B:.4f} × {COEF_B} = {result:.4f}")
            print("----------------------\n")
            
            # 询问是否继续
            again = input("继续计算吗？ (输入 y 继续，其他任意键退出): ")
            if again.lower() != 'y':
                print("程序结束。")
                break
        
        except ValueError:
            print("输入错误，请确保输入的是有效数字！\n")
        except KeyboardInterrupt:
            print("\n程序已被用户中断。")
            break

if __name__ == "__main__":
    main()