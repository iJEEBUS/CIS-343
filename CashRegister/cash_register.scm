(define tax 0.065)
(define runningTotal 0)
(define currentItem 0)
(define input 0)
(define total 0)
(define total_taxes 0)

(define (pos runningTotal condition)(

    (+ runningTotal condition)
    (if(eq? condition -1)
        (begin
            (display "\n\nSubtotal: $")
            (display runningTotal)
            (display "\nTax: $")
            (let ((total_taxes(* runningTotal tax)))
                (display total_taxes))
            (display "\nTotal: $")
            (let ((total_taxes(* runningTotal tax)))
                (let ((total(+ runningTotal total_taxes)))
                    (display total)))
            (display "\n\n")
            (exit)
        )
        (begin
            (if(eq? condition 0)
                (begin
                    (let ((greeting(display "\nScheme Point-of-Sale\nStart transaction (exit with -1)\n\nEnter a value: $")))
                        (+ greeting (let ((input(read)))((pos (+ condition runningTotal) input)))))
                )
                (begin
                    (display "Enter a value: $")
                    (let ((input(read)))((pos (+ condition runningTotal) input)))
                )
                )
        )    
    )
    )
)
