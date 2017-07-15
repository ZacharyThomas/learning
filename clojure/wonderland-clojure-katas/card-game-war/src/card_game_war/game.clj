(ns card-game-war.game)

;; feel free to use these cards or use your own data structure
(def suits [:spade ;:club :diamond :heart
            ])
(def ranks [2 3 4 5 6 7 8 9 10 11 12 13 14])
(def cards
  (for [suit suits
        rank ranks]
    [suit rank]))

;(println cards)

(defn shuffle-deck []
  (for [card cards]
    (print card)
    )
)

(defn play-round [player1-card player2-card]
  (shuffle-deck)
)

(defn play-game [player1-cards player2-cards])



