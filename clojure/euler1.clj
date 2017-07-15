(ns euler1
(:gen-class))

(defn euler1
      []
      (def muhlist (range 1000))
      (reduce + 0  (filter #(or (= 0 (mod % 3)) (= 0 (mod % 5))) muhlist)))
