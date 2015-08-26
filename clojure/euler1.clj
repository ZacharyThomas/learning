(ns euler1
(:gen-class))

(defn div-by-3-or-5?
  [num]
  (if  (or (= 0 (mod num 3) ) (= 0 (mod num 5)))
    num
    0)
)
(defn euler1
      []
      (def muhlist (range 1000))
      (reduce + 0 (map div-by-3-or-5? muhlist)) 
      
)
