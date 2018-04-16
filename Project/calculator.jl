
function main()

    function introduction()
        println("Welcome to a Julia implementation of a simple calculator!")
        println("Supported operations: + , - , * , /")
        println("Type 'clear' to clear the memory")
        println("Type 'exit' to quit")
    end

    function run()
        introduction()
        continue_running = true
        running_tally = 0
        while(continue_running)
            println("Enter a command: ")
            user_input = readline()
            split_user_input = split(user_input)

            if (length(split_user_input) != 3)
                if user_input == "quit" || user_input == "exit"
                    println("Thanks for testing out my calculator!")
                    quit()
                elseif length(split_user_input) == 2
                    operator, operand = split_user_input[1], parse(split_user_input[2])
                    if operator == "+"
                        running_tally += operand
                    elseif operator == "-"
                        running_tally -= operand
                    elseif operator == "*"
                        running_tally *= operand
                    elseif operator == "/"
                        running_tally /= operand
                    end
                else
                    println("Please enter a valid command. Remember to include spaces.")
                    continue
                end
            else
                operand_one, operand_two, operator = parse(Float64, split_user_input[1]),
                                                        parse(Float64, split_user_input[3]),
                                                        split_user_input[2]
                if operator == "+"
                    running_tally = operand_one + operand_two
                elseif operator == "-"
                    running_tally = operand_one - operand_two
                elseif operator == "*"
                    running_tally = operand_one * operand_two
                elseif operator == "/"
                    running_tally = operand_one / operand_two
                end
            end
            println(running_tally)
        end
    end
    run()
end
main()
