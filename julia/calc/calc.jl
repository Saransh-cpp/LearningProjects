function takeInput(n)
    nums = []
    for i = 1:parse(Int64, n)
        print("Enter number $i: ") 
        a = readline()
        a = parse(Float64, a)
        push!(nums, a)
    end
    println("Entered values: ", nums)
    return nums
end

function operate(operator, list)
    if operator == "+"
        return sum(list)
    elseif operator == "-"
        diff = list[1]
        for i in list
            diff -= i
        end
        return diff
    elseif operator == "*"
        mul = list[1]
        for i in list
            mul *= i
        end
        return mul
    elseif operator == "/"
        div = list[1]
        for i in list
            div /= i
        end

        if div == Inf
            throw(DivideError())
        end

        return div
    else
        throw(ArgumentError("Operator must be '+', '-', '/', or '*'."))
    end
end

function calc()
    print("Enter number of values: ")
    n = readline()

    println()
    nums = takeInput(n)

    println()
    print("Enter operator: ")
    op = readline()
    println()

    println("Result: ", operate(op, nums))
end

if abspath(PROGRAM_FILE) == @__FILE__
    calc()
end

t = Template(;
    user="Saransh",
    authors=["Saransh Chopra"],
    license="MIT",
    plugins=[
        Codecov(),
    ],
)