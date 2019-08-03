class SetOnceMappingMixin():
    """ 自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass

my_dict = SetOnceDict()
try:
    my_dict['usename'] = 'jackfrued'
    my_dict['usename'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)