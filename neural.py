import math, random

class InputNeuron:
    pass

class HiddenNeuron:
    # sets inputs and randomized weights of this hidden neuron
    def __init__(self, inputs):
        self.inputs = inputs
        self.weights = [random.uniform(-0.1, 0.1) for _ in [None] + inputs]

    # updates the activity of the neuron based on its inputs
    def update_activity(self):
        activities = [1] + [neuron.a for neuron in self.inputs]
        s = sum([w * a for w, a in zip(self.weights, activities)])
        self.a = 1 / (1 + math.exp(-s))

    # returns calculated error contribution
    def update_deltas(self, outputs, i):
        self.delta = 0
        for output in outputs:
            self.delta += output.delta * output.weights[i + 1]
        self.delta *= (self.a * (1 - self.a))

    # updates weights based on delta values
    def update_weights(self): 
        self.weights[0] += -1 * 1 * self.delta

        for i in range(1, len(self.weights)):
            self.weights[i] += (-1) * (self.inputs[i - 1].a) * self.delta
     
class OutputNeuron:
    # sets neuron with hidden its hidden neurons and randomized weights
    def __init__(self, hiddens):
        self.inputs = hiddens # these would be hidden neurons providing output to the output neurons
        self.weights = [random.uniform(-0.1, 0.1) for _ in [None] + hiddens]

    # updates activity of neuron
    def update_activity(self):
        activities = [1] + [neuron.a for neuron in self.inputs]
        s = sum([w * a for w, a in zip(self.weights, activities)])
        self.a = 1 / (1 + math.exp(-s))

    # calculates error contribution of neuron
    def update_deltas(self, target):
        self.delta = -self.a * (1 - self.a) * (target - self.a)

    # updates weights based on delta values
    def update_weights(self):
        self.weights[0] += -1 * 1 * self.delta

        for i in range(1, len(self.weights)):
            self.weights[i] += (-1) * (self.inputs[i - 1].a) * self.delta
 
class Network:
    def __init__(self, input, hidden, output):
        self.input  = [InputNeuron() for _ in range(input)]
        self.hidden = [HiddenNeuron(self.input)  for _ in range(hidden)]
        self.output = [OutputNeuron(self.hidden) for _ in range(output)]

    # given by peter
    def run(self, inputs):
        # takes list of input values and returns a list of the network's output values
        for i in range(len(inputs)): 
            self.input[i].a = inputs[i]
        for neuron in self.hidden:
            neuron.update_activity()
        for neuron in self.output:
            neuron.update_activity()
        return [neuron.a for neuron in self.output]

    def train(self, input, target):
        # just running for side effect of updating deltas
        self.run(input)

        # updates deltas for outputs and then hidden 
        for neuron, t in zip(self.output, target):
            neuron.update_deltas(t)

        for i, neuron in enumerate(self.hidden):
            neuron.update_deltas(self.output, i)

        # tweak rates to reduce error
        for output in self.output:
            output.update_weights()

        for hidden in self.hidden:
            hidden.update_weights()

# given by Peter
def experiment(sizes, inputs, targets):
    net = Network(*sizes)
    print('Before training:')
    for input in inputs:
        print(f'{input} -> {net.run(input)}')
    print('Training...')
    training = list(zip(inputs, targets))
    for epoch in range(10000):
        random.shuffle(training)
        for input, target in training:
            net.train(input, target)
    print('After training:')
    for input in inputs:
        print(f'{input} -> {net.run(input)}')

def main():
    pass
    # EXPERIMENT 1
    #experiment((2, 5, 1),
    #       [[0, 0], [0, 1], [1, 0], [1, 1]],
    #       [[0], [1], [1], [0]])

    # EXPERIMENT 2
    #experiment((3, 10, 2),
    #       [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
    #       [[0, 0], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [1, 0], [1, 1]])

if __name__ == '__main__':
    main()
