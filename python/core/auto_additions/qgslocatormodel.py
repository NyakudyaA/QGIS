# The following has been generated automatically from src/core/locator/qgslocatormodel.h
QgsLocatorModel.Role = QgsLocatorModel.CustomRole
# monkey patching scoped based enum
QgsLocatorModel.ResultDataRole = QgsLocatorModel.CustomRole.ResultData
QgsLocatorModel.Role.ResultDataRole = QgsLocatorModel.CustomRole.ResultData
QgsLocatorModel.ResultDataRole.is_monkey_patched = True
QgsLocatorModel.ResultDataRole.__doc__ = "QgsLocatorResult data"
QgsLocatorModel.ResultTypeRole = QgsLocatorModel.CustomRole.ResultType
QgsLocatorModel.Role.ResultTypeRole = QgsLocatorModel.CustomRole.ResultType
QgsLocatorModel.ResultTypeRole.is_monkey_patched = True
QgsLocatorModel.ResultTypeRole.__doc__ = "Result type"
QgsLocatorModel.ResultFilterPriorityRole = QgsLocatorModel.CustomRole.ResultFilterPriority
QgsLocatorModel.Role.ResultFilterPriorityRole = QgsLocatorModel.CustomRole.ResultFilterPriority
QgsLocatorModel.ResultFilterPriorityRole.is_monkey_patched = True
QgsLocatorModel.ResultFilterPriorityRole.__doc__ = "Result priority, used by QgsLocatorProxyModel for sorting roles."
QgsLocatorModel.ResultScoreRole = QgsLocatorModel.CustomRole.ResultScore
QgsLocatorModel.Role.ResultScoreRole = QgsLocatorModel.CustomRole.ResultScore
QgsLocatorModel.ResultScoreRole.is_monkey_patched = True
QgsLocatorModel.ResultScoreRole.__doc__ = "Result match score, used by QgsLocatorProxyModel for sorting roles."
QgsLocatorModel.ResultFilterNameRole = QgsLocatorModel.CustomRole.ResultFilterName
QgsLocatorModel.Role.ResultFilterNameRole = QgsLocatorModel.CustomRole.ResultFilterName
QgsLocatorModel.ResultFilterNameRole.is_monkey_patched = True
QgsLocatorModel.ResultFilterNameRole.__doc__ = "Associated filter name which created the result"
QgsLocatorModel.ResultFilterGroupSortingRole = QgsLocatorModel.CustomRole.ResultFilterGroupSorting
QgsLocatorModel.Role.ResultFilterGroupSortingRole = QgsLocatorModel.CustomRole.ResultFilterGroupSorting
QgsLocatorModel.ResultFilterGroupSortingRole.is_monkey_patched = True
QgsLocatorModel.ResultFilterGroupSortingRole.__doc__ = "Group results within the same filter results"
QgsLocatorModel.ResultActionsRole = QgsLocatorModel.CustomRole.ResultActions
QgsLocatorModel.Role.ResultActionsRole = QgsLocatorModel.CustomRole.ResultActions
QgsLocatorModel.ResultActionsRole.is_monkey_patched = True
QgsLocatorModel.ResultActionsRole.__doc__ = "The actions to be shown for the given result in a context menu"
QgsLocatorModel.CustomRole.__doc__ = "Custom model roles.\n\n.. note::\n\n   Prior to QGIS 3.36 this was available as QgsLocatorModel.Role\n\n.. versionadded:: 3.36\n\n" + '* ``ResultDataRole``: ' + QgsLocatorModel.CustomRole.ResultData.__doc__ + '\n' + '* ``ResultTypeRole``: ' + QgsLocatorModel.CustomRole.ResultType.__doc__ + '\n' + '* ``ResultFilterPriorityRole``: ' + QgsLocatorModel.CustomRole.ResultFilterPriority.__doc__ + '\n' + '* ``ResultScoreRole``: ' + QgsLocatorModel.CustomRole.ResultScore.__doc__ + '\n' + '* ``ResultFilterNameRole``: ' + QgsLocatorModel.CustomRole.ResultFilterName.__doc__ + '\n' + '* ``ResultFilterGroupSortingRole``: ' + QgsLocatorModel.CustomRole.ResultFilterGroupSorting.__doc__ + '\n' + '* ``ResultActionsRole``: ' + QgsLocatorModel.CustomRole.ResultActions.__doc__
# --
QgsLocatorModel.CustomRole.baseClass = QgsLocatorModel
try:
    QgsLocatorModel.__group__ = ['locator']
except NameError:
    pass
try:
    QgsLocatorAutomaticModel.__group__ = ['locator']
except NameError:
    pass
try:
    QgsLocatorProxyModel.__group__ = ['locator']
except NameError:
    pass
