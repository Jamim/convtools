from .aggregations import *
from .base import *


__all__ = ["conversion"]


class _Conversion:
    ConversionException = ConversionException
    BaseConversion = BaseConversion

    ReduceFuncs = ReduceFuncs
    and_ = And
    or_ = Or
    not_ = Not
    if_ = If

    item = GetItem
    attr = GetAttr
    call_func = staticmethod(CallFunc)

    filter = staticmethod(Filter)

    #: Shortcut to `InputArg`
    input_arg = InputArg
    inline_expr = InlineExpr
    escaped_string = EscapedString

    #: Shortcut to ``List``
    list = List
    tuple = Tuple
    set = Set
    dict = Dict

    list_comp = ListComp
    tuple_comp = TupleComp
    generator_comp = GeneratorComp
    set_comp = SetComp
    dict_comp = DictComp

    group_by = GroupBy
    reduce = Reduce
    aggregate = staticmethod(Aggregate)

    def __call__(self, obj: object):
        """Shortcut for ``ensure_conversion``"""
        return ensure_conversion(obj)

    def naive(self, obj: object):
        """Shortcut for ``NaiveConversion``"""
        return NaiveConversion(obj)

    def this(self):
        """Gets compiled into the code which returns the input: ``data_``.

        This conversion is not that useful by itself, but you can pass it to
        other conversions to feed a current input as is.

        Also, provided that you use this inside comprehension conversions,
        it references an item from an iterator."""
        return GetItem()

    def call(self, *args, **kwargs):
        return self.this().call(*args, **kwargs)


conversion = _Conversion()
