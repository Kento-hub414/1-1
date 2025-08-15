import sys
from collections import defaultdict

def prune(frontier):
    """
    frontier: [(w, v)] の候補リスト
    目的: 支配される(弱い)点を削って「良い点」だけ残す
      1) 同じ重さ w の中では価値 v が最大のものだけ残す
      2) 重さ昇順で見て、価値が前から単調増加になるように不要な点を落とす
         → (軽いのに価値も高い)点に負けている点を削除
    """
    # 1) 重さごとに価値最大を取る
    best = {}
    for w, v in frontier:
        if w not in best or best[w] < v:
            best[w] = v

    # 2) 重さ昇順に並べて、価値が前より上がるときだけ採用
    items = sorted(best.items())  # [(w, v)] を w 昇順に
    pruned = []
    max_v = -1
    for w, v in items:
        if v > max_v:
            pruned.append((w, v))
            max_v = v
        # v <= max_v なら、もっと軽い or 同じくらいで価値が高い点がすでにある → 不要
    return pruned

def solve():
    data = list(map(int, sys.stdin.read().split()))
    N, W, C = data[0], data[1], data[2]
    items = []
    idx = 3
    for _ in range(N):
        wi, vi, ci = data[idx], data[idx+1], data[idx+2]
        idx += 3
        items.append((wi, vi, ci))

    # dp[c]: コスト c ちょうどで達成できる (w, v) の「良い組」リスト（常に w ≤ W）
    dp = {0: [(0, 0)]}

    for wi, vi, ci in items:
        ndp = defaultdict(list)
        for cost, frontier in dp.items():
            # 取らない：今の前線をそのまま引き継ぐ
            ndp[cost].extend(frontier)

            # 取る：コストと重さの制約を守れるなら、新しい候補を追加
            new_cost = cost + ci
            if new_cost <= C:
                for w0, v0 in frontier:
                    w1 = w0 + wi
                    if w1 <= W:
                        ndp[new_cost].append((w1, v0 + vi))

        # 各コストで、候補を「良い点」だけに圧縮
        dp = {cost: prune(front) for cost, front in ndp.items()}

    # 最後は全コスト(≤C)の前線を見て、価値最大を答えとして出す
    ans = 0
    for front in dp.values():
        for w, v in front:
            # front は w ≤ W を満たす点のみ
            if v > ans:
                ans = v
    print(ans)

if __name__ == "__main__":
    solve()
