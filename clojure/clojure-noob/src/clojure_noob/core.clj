(ns clojure-noob.core
  (:gen-class))

(defn needs-matching-part? 
  [part]
  (re-find #"^left-" (:name part))
)

(defn make-matching-part
  [part]
  {:name (clojure.string/replace (get part :name) #"^left-" "right-") :size (get part :size)}
)

(defn symmetrize-body-parts 
  [asym-body-parts]
  (loop [remaining-asym-body-parts asym-body-parts
           final-body-parts [] ]
  (if (empty? remaining-asym-body-parts)
    final-body-parts
    (let [[part & remaining] remaining-asym-body-parts
          final-body-parts (conj final-body-parts part) ]
      (if (needs-matching-part? part)
        ( recur remaining (conj final-body-parts (make-matching-part part)))
        ( recur remaining final-body-parts)
        )
     )
    )
))

(defn better-symmetrize
  [asym-body-parts]
  (reduce (fn [final-body-parts part]
            (let [final-body-parts (conj final-body-parts part)]
              (if ( needs-matching-part? part)
                (conj final-body-parts (make-matching-part part))
                final-body-parts
                )
              )
            )
          [] asym-body-parts
          )
)
(defn hit 
  [asym-body-parts]
  (let [sym-body-parts (better-symmetrize asym-body-parts)
        body-part-size-sum (reduce + 0 (map :size sym-body-parts) )
        target (inc (rand body-part-size-sum))] 
    (loop [[part & rest] sym-body-parts
           accumulated-size (:size part)]
       (if(> accumulated-size target) 
          (do (println "You hit " (:name part))
              (println "total size was " (str accumulated-size)))
          (recur rest (+ accumulated-size (:size part)))
          )
      )
    )
)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "I'm a little teapot!")

  (def asym-hobbit-body-parts [{:name "head" :size 3}
                             {:name "left-eye" :size 1}
                             {:name "left-ear" :size 1}
                             {:name "mouth" :size 1}
                             {:name "nose" :size 1 }
                             {:name "neck" :size 2}
                             {:name "left-shoulder" :size 3}
                             {:name "left-upper-arm" :size 3}
                             {:name "chest" :size 10}
                             {:name "back" :size 10}
                             {:name "left-forearm" :size 3}
                             {:name "abdomen" :size 6}
                             {:name "left-kidney" :size 1}
                             {:name "left-hand" :size 2}
                             {:name "left-knee" :size 2}
                             {:name "left-thigh" :size 4}
                             {:name "left-lower-leg" :size 3}
                             {:name "left-achilles" :size 1}
                             {:name "left-foot" :size 2}
                             ])
  (println "Calling symmetrize...")
  (hit asym-hobbit-body-parts) 
)



