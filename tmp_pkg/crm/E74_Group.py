from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Set import Set
from .E39_Actor import Actor

if TYPE_CHECKING:
    from .E39_Actor import Actor
    from .E66_Formation import Formation
    from .E68_Dissolution import Dissolution
    from .E85_Joining import Joining
    from .E86_Leaving import Leaving

class Group(Set, Actor):
    """Group <http://www.cidoc-crm.org/cidoc-crm/E74_Group>.

    This class comprises any gatherings or organizations of human individuals or groups that act collectively or in a similar way due to any form of unifying relationship. In the wider sense this class also comprises official positions which used to be regarded in certain contexts as one actor, independent of the current holder of the office, such as the president of a country. In such cases, it may happen that the group never had more than one member. A joint pseudonym (i.e. a name that seems indicative of an individual but that is actually used as a persona by two or more people) is a particular case of E74 Group.
    A gathering of people becomes an instance of E74 Group when it exhibits organizational characteristics usually typified by a set of ideas or beliefs held in common, or actions performed together. These might be communication, creating some common artifact, a common purpose such as study, worship, business, sports, etc. Nationality can be modelled as membership in an instance of E74 Group. Married couples and other concepts of family are regarded as particular examples of E74 Group.
    """
    P107_has_current_or_former_member: list[Actor] = []
    dissolved_by: list[Dissolution] = []
    formed_by: list[Formation] = []
    gained_member_by: list[Joining] = []
    lost_member_by: list[Leaving] = []
    participated_in_formation: list[Formation] = []
