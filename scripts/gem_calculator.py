from math import sqrt


def get_gem_n(level: int) -> int:
    assert 0 < level < 21
    
    if level > 19:
        return 2 * get_gem_n(19) + get_gem_n(17) + 2 * get_gem_n(18)
    if level > 18:
        return 2 * get_gem_n(18) + get_gem_n(15) + get_gem_n(16) + get_gem_n(17)
    if level > 17:
        return 2 * get_gem_n(17) + get_gem_n(13) + get_gem_n(14) + get_gem_n(16)
    if level > 16:
        return 2 * get_gem_n(16) + get_gem_n(15)
    if level > 15:
        return 2 * get_gem_n(15) + get_gem_n(11) + get_gem_n(12) + get_gem_n(13)
    if level > 14:
        return 2 * get_gem_n(14) + get_gem_n(9) + get_gem_n(12)
    if level > 13:
        return 2 * get_gem_n(13) + get_gem_n(9) + get_gem_n(10)
    if level > 12:
        return 2 * get_gem_n(12) + get_gem_n(9)
    if level > 11:
        return 2 * get_gem_n(11) + get_gem_n(3) + get_gem_n(5) + get_gem_n(6)
    
    return 2 ** (level - 1)


def get_gem_price(base_price: float, level: int) -> float:
    """获取宝石价格

    Args:
        base_price (float): 对应1级宝石的价格（单位：万银两）
        level (int): 宝石等级

    Returns:
        float: 宝石价格
    """
    assert base_price > 0.
    return base_price * get_gem_n(level)


def get_gem_stamina(level: int) -> int:
    """获取宝石体力消耗

    Args:
        level (int): 宝石等级

    Returns:
        int: 宝石体力消耗
    """
    assert 1 < level < 21
    
    if level > 19:
        return 2 * get_gem_stamina(19) + get_gem_stamina(17) + 2 * get_gem_stamina(18)
    if level > 18:
        return 2 * get_gem_stamina(18) + get_gem_stamina(15) + get_gem_stamina(16) + get_gem_stamina(17)
    if level > 17:
        return 2 * get_gem_stamina(17) + get_gem_stamina(13) + get_gem_stamina(14) + get_gem_stamina(16)
    if level > 16:
        return 2 * get_gem_stamina(16) + get_gem_stamina(15)
    if level > 15:
        return 2 * get_gem_stamina(15) + get_gem_stamina(11) + get_gem_stamina(12) + get_gem_stamina(13)
    if level > 14:
        return 2 * get_gem_stamina(14) + get_gem_stamina(9) + get_gem_stamina(12)
    if level > 13:
        return 2 * get_gem_stamina(13) + get_gem_stamina(9) + get_gem_stamina(10)
    if level > 12:
        return 2 * get_gem_stamina(12) + get_gem_stamina(9)
    if level > 11:
        return 2 * get_gem_stamina(11) + get_gem_stamina(3) + get_gem_stamina(5) + get_gem_stamina(6)
    
    stamina: int = 0
    for i in range(2, level + 1):
        stamina += 10 * (i - 1) * 2 ** (level - i)
    return stamina


def get_star_stone_n(level: int) -> int:
    """获取星辉石数量

    Args:
        level (int): 星辉石等级

    Returns:
        int: 星辉石数量
    """
    assert 1 < level < 12
    
    if level > 10:
        return 3 * get_star_stone_n(10) + get_star_stone_n(9)
    if level > 9:
        return 3 * get_star_stone_n(9) + get_star_stone_n(6) + get_star_stone_n(7)
    if level > 8:
        return 3 * get_star_stone_n(8) + get_star_stone_n(5)
    
    return 3 ** (level - 1)


def get_star_stone_price(base_price: float, level: int) -> float:
    """获取星辉石价格

    Args:
        base_price (float): 1级星辉石的价格（单位：万银两）
        level (int): 星辉石等级

    Returns:
        float: 星辉石价格
    """
    assert base_price > 0.
    return base_price * get_star_stone_n(level)


def get_star_stone_stamina(level: int) -> int:
    """获取星辉石体力消耗

    Args:
        level (int): 星辉石等级

    Returns:
        int: 星辉石体力消耗
    """
    assert 1 < level < 12
    
    if level > 10:
        return 3 * get_star_stone_stamina(10) + get_star_stone_stamina(9)
    if level > 9:
        return 3 * get_star_stone_stamina(9) + get_star_stone_stamina(6) + get_star_stone_stamina(7)
    if level > 8:
        return 3 * get_star_stone_stamina(8) + get_star_stone_stamina(5)
    
    stamina: int = 0
    for i in range(2, level + 1):
        stamina += (30 + 30 * (i - 1)) * 3 ** (level - i)
    return stamina



def get_spirit_dust_n(level: int) -> int:
    """获取五色灵尘数量

    Args:
        level (int): 五色灵尘等级

    Returns:
        int: 五色灵尘数量
    """
    assert level > 0
    sqrt2 = sqrt(2)
    return 1 / (2 * sqrt2) * ((1 + sqrt2) ** level - (1 - sqrt2) ** level)


def get_spirit_dust_price(base_price: float, level: int) -> float:
    """获取五色灵尘价格

    Args:
        base_price (float): 1级五色灵尘的价格（单位：万银两）
        level (int): 五色灵尘等级

    Returns:
        float: 五色灵尘价格
    """
    assert base_price > 0. and level > 0
    return base_price * get_spirit_dust_n(level)


def get_spirit_dust_stamina(level: int) -> int:
    """获取五色灵尘体力消耗

    Args:
        level (int): 五色灵尘等级

    Returns:
        int: 五色灵尘体力消耗
    """
    assert level > 1
    
    stamina: int = 0
    for i in range(2, level + 1):
        stamina += (30 + 30 * (i - 1)) * 2 ** (level - i)
    for i in range(2, level - 1):
        stamina += (30 + 30 * (i - 1)) * 2 ** (level - 2 - i)
    return stamina
