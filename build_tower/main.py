def tower_builder(n_floors):
    return [f'{"*" * i:^{n_floors * 2 - 1}}' for i in range(1, n_floors * 2, 2)]
