#PyTorch Tutorial - Run each of these sections separately


# # Tensor example
import torch

tsr = torch.tensor([[10,5],[3,1]])

print(tsr)


#Tensor Derivative

import torch

x = torch.tensor(5.0, requires_grad=True)

y = x**3 +7*x + 9

y.backward()

print(x.grad)


