from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E72_Legal_Object import LegalObject

if TYPE_CHECKING:
    from ..la.Set import Set
    from .E10_Transfer_of_Custody import TransferOfCustody
    from .E11_Modification import Modification
    from .E14_Condition_Assessment import ConditionAssessment
    from .E16_Measurement import Measurement
    from .E39_Actor import Actor
    from .E3_Condition_State import ConditionState
    from .E4_Period import Period
    from .E53_Place import Place
    from .E57_Material import Material
    from .E6_Destruction import Destruction
    from .E79_Part_Addition import PartAddition
    from .E80_Part_Removal import PartRemoval
    from .E81_Transformation import Transformation
    from .E8_Acquisition import Acquisition
    from .E90_Symbolic_Object import SymbolicObject
    from .E92_Spacetime_Volume import SpacetimeVolume
    from .E93_Presence import Presence

class PhysicalThing(LegalObject):
    """Physical Thing <http://www.cidoc-crm.org/cidoc-crm/E18_Physical_Thing>.

    This class comprises all persistent physical items with a relatively stable form, human-made or natural.
    Depending on the existence of natural boundaries of such things, the CIDOC CRM distinguishes the instances of E19 Physical Object from instances of E26 Physical Feature, such as holes, rivers, pieces of land, etc. Most instances of E19 Physical Object can be moved (if not too heavy), whereas features are integral to the surrounding matter.
    An instance of E18 Physical Thing occupies not only a particular geometric space at any instant of its existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies a real, that is phenomenal, volume in spacetime. We include in the occupied space the space filled by the matter of the physical thing and all its inner spaces, such as the interior of a box. For the purpose of more detailed descriptions of the presence of an instance of E18 Physical Thing in space and time it can be associated with its specific instance of E92 Spacetime Volume by the property P196 defines (is defined by).
    The CIDOC CRM is generally not concerned with amounts of matter in fluid or gaseous states, as long as they are not confined in an identifiable way for an identifiable minimal time-span.
    """
    P46_is_composed_of: list[PhysicalThing] = []
    P46i_forms_part_of: list[PhysicalThing] = []
    added_by: list[PartAddition] = []
    assessed_by: list[ConditionAssessment] = []
    augmented_by: list[PartAddition] = []
    carries: list[SymbolicObject] = []
    changed_ownership_through: list[Acquisition] = []
    condition: list[ConditionState] = []
    contains_members_of: list[Set] = []
    current_custodian: list[Actor] = []
    current_owner: list[Actor] = []
    custody_transferred_through: list[TransferOfCustody] = []
    defines: list[SpacetimeVolume] = []
    destroyed_by: list[Destruction] = []
    diminished_by: list[PartRemoval] = []
    former_or_current_keeper: list[Actor] = []
    former_or_current_location: list[Place] = []
    former_or_current_owner: list[Actor] = []
    held_or_supported_by: list[PhysicalThing] = []
    holds_or_supports: list[PhysicalThing] = []
    made_of: list[Material] = []
    measured_by: list[Measurement] = []
    modified_by: list[Modification] = []
    occupies: list[Place] = []
    provides_reference_space_for: list[Place] = []
    removed_by: list[PartRemoval] = []
    resulted_from: list[Transformation] = []
    section: list[Place] = []
    thing_presence: list[Presence] = []
    transformed_by: list[Transformation] = []
    witnessed: list[Period] = []
