def expected_orbs(suit_type: str, n_target: int = 1, current_count: int = 0) -> float:
    """计算点到任一目标套装效果所需的附魔宝珠期望数量。

    假设同类型的各套装效果等概率出现。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        n_target (int, optional): 不同目标套装数，范围 1-该类型套装总数，默认 1
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 还需要消耗的附魔宝珠期望数量
    """
    assert -1 < current_count < 31
    
    if suit_type == "变身术":
        total: int = 80
        assert 0 < n_target <= total
    elif suit_type == "变化咒":
        total: int = 40
        assert 0 < n_target <= total
    elif suit_type == "法术追加":
        total: int = 56
        assert 0 < n_target <= total
    elif suit_type == "附加状态":
        total: int = 19
        assert 0 < n_target <= total
    else:
        raise ValueError

    p: float = n_target / total
    remaining_attempts: int = 31 - current_count

    return (1 - (1 - p) ** remaining_attempts) / p


def expected_price(suit_type: str, orb_lv: int, orb_price: int, n_target: int = 1, current_count: int = 0) -> float:
    """计算点到任一目标套装效果的宝珠及点化操作费期望总价。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        orb_lv (int): 附魔宝珠等级，可选 80、100、110、120、130、140、150、160
        orb_price (int): 单颗附魔宝珠价格，单位银两
        n_target (int, optional): 不同目标套装数，范围 1-该类型套装总数，默认 1
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 期望总价，单位银两，不含强化石成本
    """
    if orb_lv == 80:
        operation_fee = 356000
    elif orb_lv == 100:
        operation_fee = 600000
    elif orb_lv == 110:
        operation_fee = 765500
    elif orb_lv == 120:
        operation_fee = 964000
    elif orb_lv == 130:
        operation_fee = 1198500
    elif orb_lv == 140:
        operation_fee = 1472000
    elif orb_lv == 150:
        operation_fee = 1787500
    elif orb_lv == 160:
        operation_fee = 2148000
    else:
        raise ValueError

    return expected_orbs(suit_type, n_target, current_count) * (orb_price + operation_fee)


def expected_stones(suit_type: str, orb_lv: int, n_target: int = 1, current_count: int = 0) -> float:
    """计算点到任一目标套装效果所需的强化石期望数量。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        orb_lv (int): 附魔宝珠等级，可选 80、100、110、120、130、140、150、160
        n_target (int, optional): 不同目标套装数，范围 1-该类型套装总数，默认 1
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 还需要消耗的强化石期望数量
    """
    if orb_lv == 80:
        stones_per_orb = 2
    elif orb_lv == 100:
        stones_per_orb = 6
    elif orb_lv == 110:
        stones_per_orb = 8
    elif orb_lv == 120:
        stones_per_orb = 10
    elif orb_lv == 130:
        stones_per_orb = 12
    elif orb_lv == 140:
        stones_per_orb = 14
    elif orb_lv == 150:
        stones_per_orb = 16
    elif orb_lv == 160:
        stones_per_orb = 18
    else:
        raise ValueError

    return expected_orbs(suit_type, n_target, current_count) * stones_per_orb


def expected_exp(suit_type: str, orb_lv: int, n_target: int = 1, current_count: int = 0) -> float:
    """计算点到任一目标套装效果所需的人物经验期望消耗。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        orb_lv (int): 附魔宝珠等级，可选 80、100、110、120、130、140、150、160
        n_target (int, optional): 不同目标套装数，范围 1-该类型套装总数，默认 1
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 还需要消耗的人物经验期望值
    """
    if orb_lv == 80:
        exp_per_orb = 178000
    elif orb_lv == 100:
        exp_per_orb = 300000
    elif orb_lv == 110:
        exp_per_orb = 382750
    elif orb_lv == 120:
        exp_per_orb = 482000
    elif orb_lv == 130:
        exp_per_orb = 599250
    elif orb_lv == 140:
        exp_per_orb = 736000
    elif orb_lv == 150:
        exp_per_orb = 893750
    elif orb_lv == 160:
        exp_per_orb = 1074000
    else:
        raise ValueError

    return expected_orbs(suit_type, n_target, current_count) * exp_per_orb
