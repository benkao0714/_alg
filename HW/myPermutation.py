# 主函數，開始產生所有排列
def generate_permutations(total):
    explore_next(total, [])

# 遞迴探索排列
def explore_next(total, current_list):
    current_length = len(current_list)  # 記錄目前的排列長度
    if current_length == total:  # 當排列完成時
        print(current_list)  # 印出排列
        return

    # 尚未完成排列，繼續遞迴
    for candidate in range(total):  # 對於 0 到 total-1 的每個值
        if candidate not in current_list:  # 如果值尚未加入排列
            current_list.append(candidate)  # 加入排列
            explore_next(total, current_list)  # 繼續探索下一層
            current_list.pop()  # 回溯，移除最後加入的值

# 測試 generate_permutations 函數
generate_permutations(2)  # 列出 2 個元素的排列
generate_permutations(3)  # 列出 3 個元素的排列
generate_permutations(4)  # 列出 4 個元素的排列
generate_permutations(5)  # 列出 5 個元素的排列
