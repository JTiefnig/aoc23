
sensor_data = []

with open('input_9.txt') as f:
    # convert to 2d array
    lines = f.readlines()
    for line in lines:
        line_data = [int(x) for x in line.strip().split()]
        sensor_data.append(line_data)

def predict(data_set):
    divs = []
    all_zero = True
    for i in range(len(data_set)-1):
        div = data_set[i+1] - data_set[i]
        divs.append(div)
        if div != 0:
            all_zero = False
    if all_zero:
        return (data_set[0], data_set[-1])

    pred = predict(divs)
    # print("{} <{}> {}".format(data_set[0] - pred[0], data_set, data_set[-1] + pred[1]))
    return (data_set[0] - pred[0], data_set[-1] + pred[1])

sum1 = 0
sum2 = 0
for data_set in sensor_data:
    (extra_start, extra_end) = predict(data_set)
    sum2 += extra_start
    sum1 += extra_end

print(sum1)
print(sum2)


