---
layout: post
title: "[Design] Winning Games Rank (pagerank) "
comments: true
category: Design
---

### Question

> We have a history of match result of pingpong games, assume each match is <player1, player2, result, timestamp>, player1 and player2 are long type, result is a bit value (1 means player1 win).

> design a algorithm to sort the players by their possibility to win future games.

### Solution

For each play,

> winning score = score_diff \* {delay factor^(current time - winning time)};

### Pagerank

[PageRank](http://google.about.com/od/searchengineoptimization/a/pagerankexplain.htm) is what Google uses to **determine the importance of a web page**.

It determines which pages appear in search results.

Named after Larry Page.

#### Details

1. PageRank thinks of links as votes to another page.

1. It also looks at the importance of the page that contains the link.

   1. Pages with **higher PageRank** have more weight in "voting".

   1. Pages with **smaller total number of links** on the page have more weight.

#### Increase your PageRank?

If you'd like to increase your PageRank, you need to have "back-links," or other people linking to your website. You can **trade links** with other people, but make sure you only trade relevant links, and make sure you're not trading links with a **link farm**.

You can register your website with directories, such as the **Open Directory Project**, but use directories with high PageRank whenever possible.

You can create some of **your own back-links** by linking to relevant pages **within** your own website. However, remember that the number of links you create counts into the equation. Don't overdo it.
