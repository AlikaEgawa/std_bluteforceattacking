# std_bluteforceattacking

1. 任意のディレクトリに4桁整数のパスワードを設定したzipファイルを置きます
2. プログラムを実行、総当たりで解読します

`string.digits`で整数
`string.ascii_letters`で文字
`chars = string.ascii_letters + string.digits`で整数と文字の組み合わせ
`chars += '/*-+.,!#$%&()~|_'`で記号もできます

`size`で解読するパスワードの文字数指定

`range()`( )内がアタック回数
