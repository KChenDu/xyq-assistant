from math import comb


def expected_dango(n_skills: int, n_blessed_skills: int, n_locks: int = 0, total: int = 48) -> float:
    """计算达到目标赐福技能数量所需的仙露丸子期望消耗。

    Args:
        n_skills (int): 召唤兽具备且用户接受的可赐福技能数量
        n_blessed_skills (int, optional): 希望获得的赐福技能数量
        n_locks (int, optional): 已锁定的目标技能数量
        total (int, optional): 技能池总数，默认48，可根据在线确认的结果传入

    Returns:
        float: 还需要消耗的仙露丸子期望数量
    """
    assert 3 < n_skills <= total
    assert 0 < n_blessed_skills <= 4 and n_blessed_skills <= n_skills
    assert -1 < n_locks < 3 and n_locks < n_blessed_skills

    n_drawn_skills: int = 4 - n_locks
    n_required_skills: int = n_blessed_skills - n_locks
    successful_combinations: int = 0

    for n_matches in range(n_required_skills, n_drawn_skills + 1):
        successful_combinations += comb(n_skills - n_locks, n_matches) * comb(total - n_skills, n_drawn_skills - n_matches)

    return 5 ** n_locks * comb(total - n_locks, n_drawn_skills) / successful_combinations


def expected_cost(n_skills: int, n_blessed_skills: int, dango_price: float, n_locks: int = 0, total: int = 48) -> float:
    """计算达到目标赐福技能数量所需购买仙露丸子的期望银两消耗。

    Args:
        n_skills (int): 召唤兽具备且用户接受的可赐福技能数量
        n_blessed_skills (int): 希望获得的赐福技能数量
        dango_price (float): 每个仙露丸子的价格，单位银两
        n_locks (int, optional): 已锁定的目标技能数量
        total (int, optional): 技能池总数，默认48

    Returns:
        float: 期望消耗的银两
    """
    assert dango_price > 0

    return expected_dango(n_skills, n_blessed_skills, n_locks, total) * dango_price


def expected_small_dango(n_skills: int, n_blessed_skills: int, n_locks: int = 0, total: int = 48) -> str:
    """按合成比例折算仙露小丸子、体力及神兽涎的期望消耗。

    1个神兽涎、10个仙露小丸子和20点体力可合成4个仙露丸子。
    期望消耗按比例折算，保留小数；实际合成按每批4个进行。

    Args:
        n_skills (int): 召唤兽具备且用户接受的可赐福技能数量
        n_blessed_skills (int): 希望获得的赐福技能数量
        n_locks (int, optional): 已锁定的目标技能数量
        total (int, optional): 技能池总数，默认48

    Returns:
        str: 按合成比例折算的期望材料及体力消耗说明
    """
    expected_batches: float = expected_dango(n_skills, n_blessed_skills, n_locks, total) / 4

    return f"按合成比例折算，期望消耗{round(expected_batches * 10)}个仙露小丸子、{round(expected_batches)}个神兽涎和{round(expected_batches * 20)}点体力"
