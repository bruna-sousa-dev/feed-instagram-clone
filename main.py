import flet as ft

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = 'Intagram Feed'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.main()

    def main(self):
        
        def change_state_icon(e):
            if e.control.selected == False:
                e.control.selected = True
            else:
                e.control.selected = False        
            e.control.update()
        
        style_body_normal = ft.TextStyle(size = 12, color = ft.colors.BLACK, weight = ft.FontWeight.NORMAL)
        style_body_bold = ft.TextStyle(size = 12, color = ft.colors.BLACK, weight = ft.FontWeight.BOLD)
        style_body_fade = ft.TextStyle(size = 12, color = ft.colors.GREY_400, weight = ft.FontWeight.NORMAL)
        style_title_bold = ft.TextStyle(size = 14, color = ft.colors.BLACK, weight = ft.FontWeight.BOLD)

        header = ft.ListTile(
            title = ft.Text(value = 'NASA', style = style_title_bold),
            subtitle = ft.Text(value = 'A Lua!', style = style_body_normal),
            leading = ft.Image(src = '/images/NASA_logo.png', fit = ft.ImageFit.CONTAIN),
            trailing = ft.Icon(name = ft.icons.MORE_HORIZ, color = ft.colors.BLACK),
            text_color = ft.colors.BLACK,
            content_padding = ft.padding.symmetric(horizontal = 10, vertical = 0),
        )

        media = ft.Image(src = '/images/NASA_lua.webp', fit = ft.ImageFit.CONTAIN)

        actions = ft.Container(
            content = ft.ResponsiveRow(
                columns = 10,
                controls = [
                    favorite_icon := ft.IconButton(
                        col = 1,
                        icon = ft.icons.FAVORITE_BORDER,
                        icon_color = ft.colors.BLACK,
                        selected_icon = ft.icons.FAVORITE,
                        selected_icon_color = ft.colors.RED,
                        selected = False,
                        on_click = change_state_icon
                    ),
                    comments_icon := ft.IconButton(
                        col = 1,
                        icon = ft.icons.CHAT_BUBBLE_OUTLINE,
                        icon_color = ft.colors.BLACK,
                    ),
                    share_icon := ft.IconButton(
                        col = 1,
                        icon = ft.icons.SEND,
                        icon_color = ft.colors.BLACK,
                    ),
                    save_icon := ft.IconButton(
                        col = 7,
                        icon = ft.icons.BOOKMARK_BORDER,
                        icon_color = ft.colors.BLACK,
                        selected_icon = ft.icons.BOOKMARK,
                        selected_icon_color = ft.colors.BLACK,
                        alignment = ft.alignment.center_right,
                        selected = False,
                        on_click = change_state_icon
                    ),
                ],
            ),
        )

        like_for = ft.Container(
            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
            content = ft.Text(
                spans = [
                    ft.TextSpan(text = 'Curtido por ', style = style_body_normal),
                    ft.TextSpan(text = 'brunasousa.dev ', style = style_body_bold),
                    ft.TextSpan(text = 'e ', style = style_body_normal),
                    ft.TextSpan(text = '1969 outros', style = style_body_bold),    
                ],
            )
        )

        description = ft.Container(
            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
            content = ft.Column(
                spacing = 0,
                controls = [
                    ft.Text(
                        value = 'Um pequeno passo para o homem, um grande passo para a humanidade!!! 🚀🌑',
                        style = style_body_normal,
                    ),
                    ft.Text(
                        value = '55 anos atrás',
                        style = style_body_fade
                    ),
                ],
            ),
        )

        comments = ft.Container(
            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
            content = ft.Column(
                spacing = 5,
                controls = [
                    ft.Text(
                        spans = [
                            ft.TextSpan(text = 'elonmusk ', style = style_body_bold),
                            ft.TextSpan(text = 'Agora bora pra Marte! #SpaceX', style = style_body_normal),
                        ],
                    ),
                    ft.Text(value = 'Ver todos os 2.025 comentários', style = style_body_fade),
                ],
            ),
        )

        input_comments = ft.Container(
            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
            content = ft.TextField(
                hint_text = 'Adicione um comentário...',
                hint_style = style_body_fade, 
                text_style = style_body_normal,
                border = ft.InputBorder.UNDERLINE,
                multiline = False
            ),
        )
        
        layout = ft.Container(
            height = 550,
            width = 350,
            bgcolor = ft.colors.WHITE,
            border_radius = ft.border_radius.all(5),
            padding = ft.padding.all(0),
            shadow = ft.BoxShadow(blur_radius = 30, color = ft.colors.GREY_500),
            content = ft.Column(
                expand = True,
                spacing = 0,
                controls = [
                    header,
                    media,
                    actions,
                    like_for,
                    description,
                    comments,
                    input_comments
                ],
            ),
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
