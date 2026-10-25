# Received external AI review of No.40 v0.4

Received through the user on 26 October 2026. The text below is the supplied
review report, not an author execution transcript. Reviewer identity, exact
Python patch version, OS, independent source code and raw logs were not
supplied. The report specifies Python 3.13 and explicitly excludes citation
verification and literature/novelty search. No distinct-reviewer count is
inferred from this or the earlier received reports.

## Received text

40番(No.40 PitFree Corner v0.4)の監査を始めます。まず ZIP を展開し、前回までの経過も確認します。

## No.40 v0.4 監査結果

**数学面: PASS。新規性: 判定不能(INCONCLUSIVE)。公開は HOLD 継続に同意します。**

| 項目 | 判定 | 根拠 |
| --- | --- | --- |
| パッケージ整合 | PASS | SHA256SUMS の32ファイルが一致しました。v0.3 ZIP と比べ、`terrain.py`、`arrangement.py`、`verify.py`、`audit_3x3.py`、`witness.json` はバイト同一です。PROOF.md は差分があり、README が言う冒頭の状態注記だけの変更とは確認していません。 |
| 同梱スクリプト | PASS | `python -I` で4本とも通りました(面は 16/23/8、3×3 は 1120/362/233/10028、MSF は 3255 本・152985 比較)。 |
| 12セルの例 | PASS | 全セルの余裕を手で再計算し、表と一致しました。A iff \|a\|+b≥1 も、タイの順序(行優先で側方セルが B に勝つ)まで含めて合っています。 |
| 12セルの自前検査 | PASS | 作者のコードを使わず、1/80 刻み 26,001 点で式の不一致は 0 でした。シンクは全域で {A,B} のまま、4隅は A、中心は B です。 |
| 3×3 の最小性(5.1〜5.2) | PASS | 誘導経路補題と、A が隣接するときの凸性の議論に穴はありません。A が角のときは、B の5通りの配置すべてで単調性が成り立ちます。NE の場合の a 方向の単調性と b 方向の切替1回も正しいです。SW は転置で対称です。 |
| 3×3 のランダム探索 | 反例0 | 自前実装で、固定2シンクの地形を約45,000件調べて反例は 0 件でした。 |
| 4×3 の対照実験 | 検出あり | 同じ探索で反例を1件見つけました。ただし検出力は弱く、前回のレビュワー報告の 44 件には届きません。 |
| MSF 同値化(新規部分) | PASS | 最小隣接辺の重みから、記号的タイ、森の無閉路性、単一頂点カットの一意性、拡張 MST までの各主張が成り立ちます。 |
| 新規部分の注意点 | 問題なし | 共通スーパールートは証明の道具にすぎず、2つの流域の表現には別々の pendant を使う、という区別が正しく書かれています。均一な epsilon による置換も主張していません。 |

**MSF 同値化の補足**

- 拡張 MST が一意に決まるので、その部分森も一意になります。
- 有限列挙(47代表点)は補助的な確認にすぎません。連続体での同値性は、カットの議論が支えています。これは MSF_EQUIVALENCE.md 自身の書き方とも一致しています。

**確認できていない点**

- **文献の引用箇所:** Allene 定理 5.3、Cousty 2026 定理 3、Driemel の頁番号は、私は開いていません。作者側の記述のままです。
- **新規性:** 文献検索はしていません。「最小 12 に直接当たる定理は見つからなかった」という作者の記述は、不在の証明ではありません。
- **別の観点の指摘:** 4×3 の例が極端に作為的な地形かどうかは、数学の正しさとは別の話です。論文にするなら、最小性が「完全矩形・内部ソース・固定2境界シンク・共通傾斜」に限られる点を冒頭で強く書くのが安全です。
- **実行環境:** 私の実行は Python 3.13 です。作者は 3.12 を想定していますが、結果に影響はありませんでした。

次の関門は、新規性の独立監査と人間の査読です。

## Attribution limits

The approximately 45,000 accepted two-sink terrains and one positive-control
counterexample are recorded separately from the earlier reported 56.7-million
search and 44 controls. No totals, independence, detection rate or author
reproduction are inferred. The new MSF proof PASS is a received external AI
assessment; source-citation verification, historical novelty and human peer
review remain separate and are not marked PASS.
