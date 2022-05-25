import django_filters



class CustomMultipleFilterList(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            values = [v for v in value.split(',')]
            return qs.filter(**{'%s__%s' % (self.field_name, self.lookup_expr): values})
        return qs


class DiseaseTagFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='name', lookup_expr='icontains')


class DiseaseFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    tags = CustomMultipleFilterList(field_name='tags', lookup_expr='in')


