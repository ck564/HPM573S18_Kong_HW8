import CoinTossClasses as SourceCode
import scr.StatisticalClasses as Stat

# Problem 2: Comparing outcomes in a transient-state scenario (Weight 1): Present to the gambler the change and
# the percentage change in their reward if they use an unfair coin for which the probability of head is 45%.

# Parameters
PROB_HEAD = 0.5
PROB_HEAD_ADJ = 0.45
N_GAMES_IN_SET = 10
N_SETS = 1000
ALPHA = 0.05

# Simulate multiple sets of fair coin games
multiGameSetFair = SourceCode.MultipleGameSets(
    ids=range(N_SETS),
    prob_head=PROB_HEAD,
    n_games_in_a_set=N_GAMES_IN_SET)  # Create multiple sets of games with fair coin

multiGameSetFair.simulation()  # Simulate multiple sets

print('Projected average reward with fair coin: ', multiGameSetFair.get_mean_total_reward())
print('95% projection interval: ', multiGameSetFair.get_PI_total_reward(ALPHA))


# Simulate multiple sets of games with unfair coin
multiGameSetUnfair = SourceCode.MultipleGameSets(
    ids=range(N_SETS, 2*N_SETS),
    prob_head=PROB_HEAD_ADJ,
    n_games_in_a_set=N_GAMES_IN_SET)  # Create multiple sets of games with unfair coin

multiGameSetUnfair.simulation()  # Simulate multiple sets

print('Projected average reward with unfair coin: ', multiGameSetUnfair.get_mean_total_reward())
print('95% projection interval: ', multiGameSetUnfair.get_PI_total_reward(ALPHA))


# Comparative Outcomes

change = Stat.DifferenceStatIndp(
    name='Change in average reward',
    x=multiGameSetUnfair.get_all_total_rewards(),
    y_ref=multiGameSetFair.get_all_total_rewards()
)  # Obtain change in average reward

# percentChange = Stat.RelativeDifferenceIndp(
#     name='Percent change in average reward',
#     x=multiGameSetUnfair.get_all_total_rewards(),
#     y_ref=multiGameSetFair.get_all_total_rewards()
# )  # Obtain percent change in average reward


print('Change in average reward: ', change.get_mean())
print('95% projection interval: ', change.get_t_CI(ALPHA))
# print('Percent change in average reward: ', percentChange.get_mean())
# print('95% confidence interval: ', percentChange.get_t_CI(ALPHA))


