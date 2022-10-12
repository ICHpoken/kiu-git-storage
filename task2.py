def warn_the_sheep(queue):
    if queue[::-1].index('wolf') == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        index_wolf = str(queue.index('wolf'))
        return 'Oi! Sheep number ' + index_wolf + '! You are about to be eaten by a wolf!'