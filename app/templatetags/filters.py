from django import template
# HTMLないで使いたいテンプレートタグを作成する場合は必ず必要

register = template.Library()
# registerはなんでもいい（名前）

@register.simple_tag
# .simple_tagが必要
def multiply(value1, value2):
       return value1 * value2

# HTML内で行いたい簡易的な処理
# humanaize もテンプレートタグ