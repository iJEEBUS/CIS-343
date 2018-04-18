; A very simple calculator program that is written in mit-scheme.
; It is able to take in the user input, add that to the running total
; before calculating the tax on the entire order and presenting the user
; with a total amount do. 
; At the end of execution the program terminates gracefully
;
; Author(s): Ronald Rounsifer
; Date: 04.17.2018

; definition of functions 
; to be used in the program
(define tax 0.065)
(define runningTotal 0)
(define currentItem 0)
(define input 0)
(define total 0)
(define total_taxes 0)
; This function allows us to round off the 
; any number inputted (z) to the specified number
; of decimal spaces (n)
(define (roundOff z n)
  (let ((power (expt 10 n)))
    (/ (round (* power z)) power)))

; Main body of the program
(define (pos runningTotal condition)(
                                     
    ; Add the inputted number to the running total
    (+ runningTotal condition)
                                     
    ; When -1 is entered, the tax and final price are calculated before being displayed
    (if(eq? condition -1)
        (begin
            (display "\n\nSubtotal: $")
            (display (roundOff runningTotal 2))
            (display "\nTax: $")
            (let ((total_taxes(* runningTotal tax)))
                (display (roundOff total_taxes 2) ))
            (display "\nTotal: $")
            (let ((total_taxes(* runningTotal tax)))
                (let ((total(+ runningTotal total_taxes)))
                    (display (roundOff total 2))))
            (display "\n\n")
            (exit)
        )
       ; When the user enters a number to add
        (begin
            ; If this is the first iteration of the program
            ; display a greeting message
            (if(eq? condition 0)
                (begin
                    (let ((greeting(display "\nScheme Point-of-Sale\nStart transaction (exit with -1)\n\nEnter a value: $")))
                        (+ greeting (let ((input(read)))((pos (+ condition runningTotal) input)))))
                )
                ; Prompt the user for a dollar amount
                ; Recursively calls the pos function to continue
                ; the user point-of-sale experience
                (begin
                    (display "Enter a value: $")
                    (let ((input(read)))((pos (+ condition runningTotal) input)))
                )
                )
        )    
    )
    )
)
