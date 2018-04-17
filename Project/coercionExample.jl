function coercionExample()
    x::Int8 = 100
    println("Type of x: $(typeof(x))")
    x += 2.0
    println("Type of x after addition with float: $(typeof(x))")
end
coercionExample()
