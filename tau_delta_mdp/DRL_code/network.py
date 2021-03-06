import torch
from torch import nn
from torch.distributions import Normal
import torch.nn.functional as F
import utility

class SACActor(nn.Module):

    def __init__(self, state_shape, action_shape):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(state_shape[0], 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 2 * action_shape[0]),
        )

    def forward(self, states):
        return torch.tanh(self.net(states).chunk(2, dim=-1)[0])

    def sample(self, states):
        means, log_stds = self.net(states).chunk(2, dim=-1)
        return utility.reparameterize(means, log_stds.clamp(-20, 2))


class SACCritic(nn.Module):

    def __init__(self, state_shape, action_shape):
        super().__init__()

        self.net1 = nn.Sequential(
            nn.Linear(state_shape[0] + action_shape[0], 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 1),
        )
        self.net2 = nn.Sequential(
            nn.Linear(state_shape[0] + action_shape[0], 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 1),
        )

    def forward(self, states, actions):
        x = torch.cat([states, actions], dim=-1)
        return self.net1(x), self.net2(x)

# class DDPGActor(nn.Module):

#     def __init__(self, state_shape, action_shape):
#         super().__init__()

#         self.net = nn.Sequential(
#             nn.Linear(state_shape[0], 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, action_shape[0]),
#         )

#     def forward(self, states):
#         return torch.tanh(self.net(states))

#     def sample(self, states):
#         return self(states)

# class DDPGCritic(nn.Module):

#     def __init__(self, state_shape, action_shape):
#         super().__init__()

#         self.net = nn.Sequential(
#             nn.Linear(state_shape[0] + action_shape[0], 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 1),
#         )

#     def forward(self, states, actions):
#         x = torch.cat([states, actions], dim=-1)
#         return self.net(x)

# class TD3Actor(nn.Module):

#     def __init__(self, state_shape, action_shape):
#         super().__init__()

#         self.net = nn.Sequential(
#             nn.Linear(state_shape[0], 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, action_shape[0]),
#         )

#     def forward(self, states):
#         return torch.tanh(self.net(states))

#     def sample(self, states):
#         return self(states)

# class TD3Critic(nn.Module):

#     def __init__(self, state_shape, action_shape):
#         super().__init__()

#         self.net1 = nn.Sequential(
#             nn.Linear(state_shape[0] + action_shape[0], 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 1),
#         )
#         self.net2 = nn.Sequential(
#             nn.Linear(state_shape[0] + action_shape[0], 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 256),
#             nn.ReLU(inplace=True),
#             nn.Linear(256, 1),
#         )

#     def forward(self, states, actions):
#         x = torch.cat([states, actions], dim=-1)
#         return self.net1(x), self.net2(x)

#     def Q1(self, states, actions):
#         x = torch.cat([states, actions], dim=-1)
#         return self.net1(x)