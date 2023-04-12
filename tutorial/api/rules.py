"""
Rules definitions.
"""
import crum
import rules
from edx_rbac.utils import get_decoded_jwt, request_user_has_implicit_access_via_jwt


def _user_has_implicit_access_via_feature_role(user, context, feature_role):  # pylint: disable=unused-argument
    """
    Check that the requesting user has implicit access (from a JWT) 
    to the given context via the given feature role.
    Returns:
        bool: True if the user has access.
    """
    if not context:
        return False
    request = crum.get_current_request()
    decoded_jwt = get_decoded_jwt(request)
    return request_user_has_implicit_access_via_jwt(
        decoded_jwt,
        feature_role,
        context,
    )


@rules.predicate
def has_publication_admin_access(user, context):
    return _user_has_implicit_access_via_feature_role(user, context, 'publication_admin')


@rules.predicate
def has_publication_user_access(user, context):
    return _user_has_implicit_access_via_feature_role(user, context, 'publication_user')


@rules.predicate
def has_article_admin_access(user, context):
    return _user_has_implicit_access_via_feature_role(user, context, 'article_admin')


@rules.predicate
def has_article_user_access(user, context):
    return _user_has_implicit_access_via_feature_role(user, context, 'article_user')


rules.add_perm('articles.can_read', has_article_admin_access | has_article_user_access)
rules.add_perm('articles.can_write', has_article_admin_access)
