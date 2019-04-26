"""
    Word Pressへの簡易投稿

    Author: たっきん

    Note: 依存パッケージ
        ・python-wordpress-xmlrpc

"""

import sys

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.exceptions import InvalidCredentialsError
from wordpress_xmlrpc.exceptions import ServerConnectionError
from wordpress_xmlrpc.exceptions import XmlrpcDisabledError
from wordpress_xmlrpc.methods.posts import NewPost

# 投稿ステータス定義
POST_STATUS_DRAFT = "draft"
POST_STATUS_PRIVATE = "private"
POST_STATUS_PENDING = "pending"
POST_STATUS_PUBLISH = "publish"


def post_wordpress(loginid, loginpw, domain, title, content, post_tag,
                   category, post_status):
    """Word Pressへの簡易投稿

    Args:
        loginid (str): Your login ID.
        loginpw (str): Your login PassWord.
        domain (str): Your WordPress domain name.
        title (str): Post title.
        content (str): Post contents.
        post_tag (str[]): Post tag.
        category (str[]): Post category.
        post_status (str): Post status.

    Returns:
        None

    """

    url = "http://" + domain + "/xmlrpc.php"

    try:
        wp = Client('%s/xmlrpc.php' % url, loginid, loginpw)
    except ServerConnectionError:
        sys.exit("Cannot Connect to the server. Please check your network.")
    except:
        sys.exit("Cannot find configuration!")

    post = WordPressPost()
    post.title = title
    post.content = content
    post.terms_names = {"post_tag": post_tag, "category": category}
    post.status = post_status

    try:
        wp.call(NewPost(post))
    except InvalidCredentialsError:
        sys.exit("Username or Password is incorrect")
    except XmlrpcDisabledError:
        sys.exit("XML-RPC services are disabled in WordPress")

    print("Finish post！")


if __name__ == "__main__":

    loginid = input("Input your login ID: ")
    loginpw = input("Input your login PW: ")
    domain = input("Input your domain: ")

    title = "たっきんブログ投稿テスト"
    content = "ブログの内容です"

    post_tag = []   # タグ
    category = []   # カテゴリー

    post_status = POST_STATUS_DRAFT     # 投稿ステータス

    post_wordpress(loginid, loginpw, domain, title,
                   content, post_tag, category, post_status)
