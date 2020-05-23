inputs = [1, 2, 3, 2.5]

weights = [
        [ 0.2, 0.8, -0.5, 1 ],
        [ 0.5, -0.91, 0.26, -0.5 ],
        [ -0.26, -0.27, 0.17, 0.87 ]
    ]

biases = [2, 3, 0.5]

layer_output = []
for (neuron_bias, neuron_weights) in zip(biases, weights):
    neuron_output = 0
    for (n_input, weight) in zip(inputs, neuron_weights): 
        neuron_output = neuron_output + (n_input * weight)
    layer_output.append(neuron_output+neuron_bias)

print(layer_output)