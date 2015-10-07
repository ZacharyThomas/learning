(ns alphabet-cipher.coder)

(defn encode-thing 
[keychar messchar]
(def char-with-offset (+ (int keychar) (- (int messchar) 97)))
(if (> char-with-offset (int \z) ) 
  (char  (- char-with-offset 26) )
  (char char-with-offset)
  )
)

(defn encode [keyword message]
  (->> keyword
     (cycle)
     (take (count message))
     (apply str)
     (map encode-thing message)
     (apply str)
 )
)

(defn decode-thing 
  [keychar messchar]
  (def offset (if (> (int keychar) (int messchar) ) 
                ;; offset is weird 
                (do (-> keychar
                        (int)
                        (- (int messchar))
                        (->> (- 123))
                        (char)
                        ))

                ;; offset is fine
                (do (-> messchar
                        (int) 
                        (- (int keychar) )
                        (+ (int \a) )
                        (char)
                    )
                    ) 
                )
    )
  offset
)


(defn decode [keyword message]
  (def keychar (apply str (take (count message) (cycle keyword) )))
  (apply str ( map decode-thing keychar message)) 


  )

(defn decycle [cycled-string] 
  (loop [loop-num 1]
        (if (= (apply str (take (count cycled-string) (cycle (take loop-num cycled-string)))) cycled-string)
          (take loop-num cycled-string)
          (do (if (> loop-num (count cycled-string))
                "yes"
                (recur (+ loop-num 1))))
        )
        )
)

(defn decipher [cypher message]
  (apply str (decycle (apply str (map decode-thing message cypher))))

)

