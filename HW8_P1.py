import CoinTossClasses as SourceCode
import scr.StatisticalClasses as Stat

# Problem 1: Comparing outcomes in a steady-state scenario (Weight 1): Present to the casino’s owner the change and the
# percentage change in their reward if they use an unfair coin for which the probability of head is 45%.

# Parameters
PROB_HEAD = 0.5
PROB_HEAD_ADJ = 0.45
N_GAMES = 1000
ALPHA = 0.05

# Simulate set of fair coin games
gameSetFair = SourceCode.SetOfGames(id=1, prob_head=PROB_HEAD, n_games=N_GAMES)  # Create set of fair coin games

fairOutcomes = gameSetFair.simulation()  # Simulate set of fair coin games

print('Average reward for fair coin: ', fairOutcomes.get_ave_reward())  # Obtain avg reward for set of fair coin games
print('95% confidence interval: ', fairOutcomes.get_CI_reward(ALPHA))

# Simulate set of games with unfair coin
gameSetUnfair = SourceCode.SetOfGames(id=2, prob_head=PROB_HEAD_ADJ, n_games=N_GAMES)  # Create set of games w/ unfair coin

unfairOutcomes = gameSetUnfair.simulation()  # Simulate set of games with unfair coin

print('Average reward for unfair coin: ', unfairOutcomes.get_ave_reward())  # Obtain avg reward for set of games w/ unfair coin
print('95% confidence interval: ', unfairOutcomes.get_CI_reward(ALPHA))

# Comparative Outcomes

change = Stat.DifferenceStatIndp(
    name='Change in average reward',
    x=unfairOutcomes.get_rewards(),
    y_ref=fairOutcomes.get_rewards()
)  # Obtain change in average reward

percentChange = Stat.RelativeDifferenceIndp(
    name='Percent change in average reward',
    x=unfairOutcomes.get_rewards(),
    y_ref=fairOutcomes.get_rewards()
)  # Obtain percent change in average reward


print('Change in average reward: ', change.get_mean())
print('95% confidence interval: ', change.get_t_CI(ALPHA))
print('Percent change in average reward: ', percentChange.get_mean())
print('95% confidence interval: ', percentChange.get_t_CI(ALPHA))





