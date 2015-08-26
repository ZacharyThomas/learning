(ns euler2
(:gen-class))

(defn euler2
  []
  ;; Strategy : Apply reduce to 2-seq until it surpasses 4mil
  (loop [fib-seq [1 2] 
         even-sum 0]
    (if (< (get fib-seq 1) 4000000)
      (do 
        (if (= (mod (get fib-seq 1) 2 ) 0)
           (recur [(get fib-seq 1) (reduce + fib-seq)] (+ even-sum (get fib-seq 1)))
           (recur [(get fib-seq 1) (reduce + fib-seq)] even-sum))
      )
      even-sum
      )
))
