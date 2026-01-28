from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel, Field


class E1_CRM_Entity(BaseModel):
    """CRM Entity <http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity>.

    This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.
    It is an abstract concept providing for three general properties:.
    Identification by name or appellation, and in particular by a preferred identifier.
    Classification by type, allowing further refinement of the specific subclass an instance belongs to.
    Attachment of free text and other unstructured data for the expression of anything not captured by formal properties.
    All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity"
    P129i_is_subject_of: E89_Propositional_Object | list[E89_Propositional_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P129i_is_subject_of"})
    P136i_supported_type_creation: E83_Type_Creation | list[E83_Type_Creation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P136i_supported_type_creation"})
    P137_exemplifies: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P137_exemplifies"})
    P138i_has_representation: E36_Visual_Item | list[E36_Visual_Item] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P138i_has_representation"})
    P140i_was_attributed_by: E13_Attribute_Assignment | list[E13_Attribute_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P140i_was_attributed_by"})
    P141i_was_assigned_by: E13_Attribute_Assignment | list[E13_Attribute_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P141i_was_assigned_by"})
    P15i_influenced: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P15i_influenced"})
    P17i_motivated: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P17i_motivated"})
    P1_is_identified_by: E41_Appellation | list[E41_Appellation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P1_is_identified_by"})
    P2_has_type: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P2_has_type"})
    P3_has_note: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P3_has_note"})
    P41i_was_classified_by: E17_Type_Assignment | list[E17_Type_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P41i_was_classified_by"})
    P48_has_preferred_identifier: E42_Identifier | list[E42_Identifier] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P48_has_preferred_identifier"})
    P62i_is_depicted_by: E24_Physical_Human_Made_Thing | list[E24_Physical_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P62i_is_depicted_by"})
    P67i_is_referred_to_by: E89_Propositional_Object | list[E89_Propositional_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P67i_is_referred_to_by"})
    P70i_is_documented_in: E31_Document | list[E31_Document] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P70i_is_documented_in"})
    P71i_is_listed_in: E32_Authority_Document | list[E32_Authority_Document] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P71i_is_listed_in"})


class E2_Temporal_Entity(E1_CRM_Entity):
    """Temporal Entity <http://www.cidoc-crm.org/cidoc-crm/E2_Temporal_Entity>.

    This class comprises all phenomena, such as the instances of E4 Periods and E5 Events, which happen over a limited extent in time. This extent in time must be contiguous, i.e., without gaps. In case the defining kinds of phenomena for an instance of E2 Temporal Entity cease to happen, and occur later again at another time, we regard that the former instance of E2 Temporal Entity has ended and a new instance has come into existence. In more intuitive terms, the same event cannot happen twice.
    In some contexts, such phenomena are also called perdurants. This class is disjoint from E77 Persistent Item and is an abstract class that typically has no direct instances. E2 Temporal Entity is specialized into E4 Period, which applies to a particular geographic area (defined with a greater or lesser degree of precision), and E3 Condition State, which applies to instances of E18 Physical Thing.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E2_Temporal_Entity"
    P173_starts_before_or_with_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P173_starts_before_or_with_the_end_of"})
    P173i_ends_after_or_with_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P173i_ends_after_or_with_the_start_of"})
    P174_starts_before_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P174_starts_before_the_end_of"})
    P174i_ends_after_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P174i_ends_after_the_start_of"})
    P175_starts_before_or_with_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P175_starts_before_or_with_the_start_of"})
    P175i_starts_after_or_with_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P175i_starts_after_or_with_the_start_of"})
    P176_starts_before_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P176_starts_before_the_start_of"})
    P176i_starts_after_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P176i_starts_after_the_start_of"})
    P182_ends_before_or_with_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P182_ends_before_or_with_the_start_of"})
    P182i_starts_after_or_with_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P182i_starts_after_or_with_the_end_of"})
    P183_ends_before_the_start_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P183_ends_before_the_start_of"})
    P183i_starts_after_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P183i_starts_after_the_end_of"})
    P184_ends_before_or_with_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P184_ends_before_or_with_the_end_of"})
    P184i_ends_with_or_after_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P184i_ends_with_or_after_the_end_of"})
    P185_ends_before_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P185_ends_before_the_end_of"})
    P185i_ends_after_the_end_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P185i_ends_after_the_end_of"})
    P4_has_time_span: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P4_has_time-span"})


class E3_Condition_State(E2_Temporal_Entity):
    """Condition State <http://www.cidoc-crm.org/cidoc-crm/E3_Condition_State>.

    This class comprises the states of objects characterised by a certain condition over a time-span.
    An instance of this class describes the prevailing physical condition of any material object or feature during a specific instance of E52 Time-Span. In general, the time-span for which a certain condition can be asserted may be shorter than the real time-span, for which this condition held.
    The nature of that condition can be described using P2 has type. For example, the instance of E3 Condition State “condition of the SS Great Britain between 22-nd September 1846 and 27-th August 1847” can be characterized as an instance “wrecked” of E55 Type.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E3_Condition_State"
    P35i_was_identified_by: E14_Condition_Assessment | list[E14_Condition_Assessment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P35i_was_identified_by"})
    P44i_is_condition_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P44i_is_condition_of"})
    P5_consists_of: E3_Condition_State | list[E3_Condition_State] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P5_consists_of"})
    P5i_forms_part_of: E3_Condition_State | list[E3_Condition_State] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P5i_forms_part_of"})


class E52_Time_Span(E1_CRM_Entity):
    """Time-Span <http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span>.

    This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end and a duration.
    Instances of E52 Time-Span have no semantic connotations about phenomena happening within the temporal extent they represent. They do not convey any meaning other than a positioning on the “time-line” of chronology. The actual extent of an instance of E52 Time-Span can be approximated by properties of E52 Time-Span giving inner and outer bounds in the form of dates (instances of E61 Time Primitive). Comparing knowledge about time-spans is fundamental for chronological reasoning.
    Some instances of E52 Time-Span may be defined as the actual, in principle observable, temporal extent of instances of E2 Temporal Entity via the property P4 has time-span (is time-span of): E52 Time-Span. They constitute phenomenal time-spans as defined in CRMgeo (Doerr &amp; Hiebel 2013). Since our knowledge of history is imperfect and physical phenomena are fuzzy in nature, the extent of phenomenal time-spans can only be described in approximation. An extreme case of approximation, might, for example, define an instance of E52 Time-Span having unknown beginning, end and duration. It may, nevertheless, be associated with other descriptions by which we can infer knowledge about it, such as in relative chronologies.
    Some instances of E52 may be defined precisely as representing a declaration of a temporal extent, as, for instance, done in a business contract. They constitute declarative time-spans as defined in CRMgeo (Doerr &amp; Hiebel 2013) and can be described via the property E61 Time Primitive P170 defines time (time is defined by): E52 Time-Span.
    When used as a common E52 Time-Span for two events, it will nevertheless describe them as being simultaneous, even if nothing else is known.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span"
    P160i_is_temporal_projection_of: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P160i_is_temporal_projection_of"})
    P164i_temporally_specifies: E93_Presence | list[E93_Presence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P164i_temporally_specifies"})
    P170i_time_is_defined_by: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P170i_time_is_defined_by"})
    P191_had_duration: E54_Dimension | list[E54_Dimension] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P191_had_duration"})
    P4i_is_time_span_of: E2_Temporal_Entity | list[E2_Temporal_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P4i_is_time-span_of"})
    P79_beginning_is_qualified_by: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P79_beginning_is_qualified_by"})
    P80_end_is_qualified_by: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P80_end_is_qualified_by"})
    P81_ongoing_throughout: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P81_ongoing_throughout"})
    P81a_end_of_the_begin: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P81a_end_of_the_begin"})
    P81b_begin_of_the_end: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P81b_begin_of_the_end"})
    P82_at_some_time_within: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P82_at_some_time_within"})
    P82a_begin_of_the_begin: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P82a_begin_of_the_begin"})
    P82b_end_of_the_end: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P82b_end_of_the_end"})
    P86_falls_within: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P86_falls_within"})
    P86i_contains: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P86i_contains"})


class E53_Place(E1_CRM_Entity):
    """Place <http://www.cidoc-crm.org/cidoc-crm/E53_Place>.

    This class comprises extents in the natural space we live in, in particular on the surface of the Earth, in the pure sense of physics: independent from temporal phenomena and matter. They may serve describing the physical location of things or phenomena or other areas of interest. Geometrically, instances of E53 Place constitute single contiguous areas or a finite aggregation of disjoint areas in space which are each individually contiguous. They may have fuzzy boundaries.
    The instances of E53 Place are usually determined by reference to the position of “immobile” objects such as buildings, cities, mountains, rivers, or dedicated geodetic marks, but may also be determined by reference to mobile objects. A Place can be determined by combining a frame of reference and a location with respect to this frame.
    It is sometimes argued that instances of E53 Place are best identified by global coordinates or absolute reference systems. However, relative references are often more relevant in the context of cultural documentation and tend to be more precise. In particular, we are often interested in position in relation to large, mobile objects, such as ships. For example, the Place at which Nelson died is known with reference to a large mobile object – H.M.S Victory. A resolution of this Place in terms of absolute coordinates would require knowledge of the movements of the vessel and the precise time of death, either of which may be revised, and the result would lack historical and cultural relevance.
    Any instance of E18 Physical Thing can serve as a frame of reference for an instance of E53 Place. This may be documented using the property P157 is at rest relative to (provides reference space for).
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E53_Place"
    P121_overlaps_with: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P121_overlaps_with"})
    P122_borders_with: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P122_borders_with"})
    P156i_is_occupied_by: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P156i_is_occupied_by"})
    P157_is_at_rest_relative_to: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P157_is_at_rest_relative_to"})
    P161i_is_spatial_projection_of: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P161i_is_spatial_projection_of"})
    P167i_includes: E93_Presence | list[E93_Presence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P167i_includes"})
    P168_place_is_defined_by: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P168_place_is_defined_by"})
    P171_at_some_place_within: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P171_at_some_place_within"})
    P172_contains: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P172_contains"})
    P189_approximates: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P189_approximates"})
    P189i_is_approximated_by: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P189i_is_approximated_by"})
    P197i_was_partially_covered_by: E93_Presence | list[E93_Presence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P197i_was_partially_covered_by"})
    P26i_was_destination_of: E9_Move | list[E9_Move] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P26i_was_destination_of"})
    P27i_was_origin_of: E9_Move | list[E9_Move] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P27i_was_origin_of"})
    P53i_is_former_or_current_location_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P53i_is_former_or_current_location_of"})
    P54i_is_current_permanent_location_of: E19_Physical_Object | list[E19_Physical_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P54i_is_current_permanent_location_of"})
    P55i_currently_holds: E19_Physical_Object | list[E19_Physical_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P55i_currently_holds"})
    P59i_is_located_on_or_within: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P59i_is_located_on_or_within"})
    P74i_is_current_or_former_residence_of: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P74i_is_current_or_former_residence_of"})
    P7i_witnessed: E4_Period | list[E4_Period] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P7i_witnessed"})
    P89_falls_within: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P89_falls_within"})
    P89i_contains: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P89i_contains"})


class E54_Dimension(E1_CRM_Entity):
    """Dimension <http://www.cidoc-crm.org/cidoc-crm/E54_Dimension>.

    This class comprises quantifiable properties that can be measured by some calibrated means and can be approximated by values, i.e., by points or regions in a mathematical or conceptual space, such as natural or real numbers, RGB values etc.
    An instance of E54 Dimension represents the empirical or theoretically derived quantity, including the precision tolerances resulting from the particular method or calculation. The identity of an instance of E54 Dimension depends on the method of its determination because each method may produce different values even when determining comparable qualities. For instance, the wingspan of a bird alive or dead is a different dimension. Thermoluninescence dating and Rehydroxylation [RHX] dating are different dimensions of temporal distance from now, even if they aim at dating the same object. The method of determination should be expressed using the property P2 has type (is type of). Note that simple terms such as “diameter” or “length” are normally insufficient to unambiguously describe a respective dimension. In contrast, “maximum linear extent” may be sufficient.
    The properties of the class E54 Dimension allow for expressing the numerical approximation of the values of instances of E54 Dimension adequate to the precision of the applied method of determination. If the respective quantity belongs to a non-discrete space according to the laws of physics, such as spatial distances, it is recommended to record them as approximations by intervals or regions of indeterminacy enclosing the assumed true values. For instance, a length of 5 cm may be recorded as 4.5-5.5 cm, according to the precision of the respective observation. Note, that comparability of values described in different units depends critically on the representation as value regions.
    Numerical approximations in archaic instances of E58 Measurement Unit used in historical records should be preserved. Equivalents corresponding to current knowledge should be recorded as additional instances of E54 Dimension, as appropriate.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E54_Dimension"
    P191i_was_duration_of: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P191i_was_duration_of"})
    P40i_was_observed_in: E16_Measurement | list[E16_Measurement] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P40i_was_observed_in"})
    P43i_is_dimension_of: E70_Thing | list[E70_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P43i_is_dimension_of"})
    P90_has_value: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P90_has_value"})
    P90a_has_lower_value_limit: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P90a_has_lower_value_limit"})
    P90b_has_upper_value_limit: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P90b_has_upper_value_limit"})
    P91_has_unit: E58_Measurement_Unit | list[E58_Measurement_Unit] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P91_has_unit"})


class E77_Persistent_Item(E1_CRM_Entity):
    """Persistent Item <http://www.cidoc-crm.org/cidoc-crm/E77_Persistent_Item>.

    This class comprises items that have persistent characteristics of structural nature substantially related to their identity and their integrity, sometimes known as “endurants” in philosophy. Persistent Items may be physical entities, such as people, animals or things, conceptual entities such as ideas, concepts, products of the imagination or even names.
    Instances of E77 Persistent Item may be present or be part of interactions in different periods or events. They can repeatedly be recognized at disparate occasions during their existence by characteristics of structural nature. The respective characteristics need not be exactly the same during all the existence of an instance of E77 Persistent Item. Often, they undergo gradual change, still bearing some similarities with that of previous times, or disappear completely and new emerge. For instance, a person, from the time of being born on, will gradually change all its features and acquire new ones, such as a scar. Even the DNA in different body cells will develop defects and mutations. Nevertheless, relevant characteristics used should be sufficiently similar to recognize the instance for some substantial period of time.
    The more specific criteria that determine the identity of instances of subclasses of E77 Persistent Item may vary considerably and are described or referred to in the respective scope notes. The decision about which exact criteria to use depends on whether the observable behaviour of the respective part of reality such confined conforms to the reasoning the user is interested in. For example, a building can be regarded as no longer existing if it is dismantled and the materials reused in a different configuration. On the other hand, human beings go through radical and profound changes during their life-span, affecting both material composition and form, yet preserve their identity by other criteria, such as being bodily separated from other persons. Similarly, inanimate objects may be subject to exchange of parts and matter. On the opposite, the identity of a (version of a) text of a scientific publication is given by the exact arrangement of its relevant symbols.
    The main classes of objects that fall outside the scope of the E77 Persistent Item class are temporal objects such as periods, events and acts, and descriptive properties.
    An instance of E77 Persistent Item does not require actual knowledge of the identifying features of the instance being currently known. There may be cases, where the actual identifying features of an instance of E77 Persistent Item are not decidable at a particular state of knowledge.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E77_Persistent_Item"
    P12i_was_present_at: E5_Event | list[E5_Event] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P12i_was_present_at"})
    P92i_was_brought_into_existence_by: E63_Beginning_of_Existence | list[E63_Beginning_of_Existence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P92i_was_brought_into_existence_by"})
    P93i_was_taken_out_of_existence_by: E64_End_of_Existence | list[E64_End_of_Existence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P93i_was_taken_out_of_existence_by"})


class E39_Actor(E77_Persistent_Item):
    """Actor <http://www.cidoc-crm.org/cidoc-crm/E39_Actor>.

    This class comprises people, either individually or in groups, who have the potential to perform intentional actions of kinds for which someone may be held responsible.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E39_Actor"
    P105i_has_right_on: E72_Legal_Object | list[E72_Legal_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P105i_has_right_on"})
    P107i_is_current_or_former_member_of: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P107i_is_current_or_former_member_of"})
    P109i_is_current_or_former_curator_of: E78_Curated_Holding | list[E78_Curated_Holding] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P109i_is_current_or_former_curator_of"})
    P11i_participated_in: E5_Event | list[E5_Event] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P11i_participated_in"})
    P143i_was_joined_by: E85_Joining | list[E85_Joining] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P143i_was_joined_by"})
    P145i_left_by: E86_Leaving | list[E86_Leaving] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P145i_left_by"})
    P14i_performed: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P14i_performed"})
    P22i_acquired_title_through: E8_Acquisition | list[E8_Acquisition] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P22i_acquired_title_through"})
    P23i_surrendered_title_through: E8_Acquisition | list[E8_Acquisition] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P23i_surrendered_title_through"})
    P28i_surrendered_custody_through: E10_Transfer_of_Custody | list[E10_Transfer_of_Custody] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P28i_surrendered_custody_through"})
    P29i_received_custody_through: E10_Transfer_of_Custody | list[E10_Transfer_of_Custody] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P29i_received_custody_through"})
    P49i_is_former_or_current_keeper_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P49i_is_former_or_current_keeper_of"})
    P50i_is_current_keeper_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P50i_is_current_keeper_of"})
    P51i_is_former_or_current_owner_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P51i_is_former_or_current_owner_of"})
    P52i_is_current_owner_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P52i_is_current_owner_of"})
    P74_has_current_or_former_residence: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P74_has_current_or_former_residence"})
    P75_possesses: E30_Right | list[E30_Right] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P75_possesses"})
    P76_has_contact_point: E41_Appellation | list[E41_Appellation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P76_has_contact_point"})


class E70_Thing(E77_Persistent_Item):
    """Thing <http://www.cidoc-crm.org/cidoc-crm/E70_Thing>.

    This general class comprises discrete, identifiable, instances of E77 Persistent Item that are documented as single units, that either consist of matter or depend on being carried by matter and are characterized by relative stability.
    They may be intellectual products or physical things. They may for instance have a solid physical form, an electronic encoding, or they may be a logical concept or structure.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E70_Thing"
    P101_had_as_general_use: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P101_had_as_general_use"})
    P130_shows_features_of: E70_Thing | list[E70_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P130_shows_features_of"})
    P130i_features_are_also_found_on: E70_Thing | list[E70_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P130i_features_are_also_found_on"})
    P16i_was_used_for: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P16i_was_used_for"})
    P43_has_dimension: E54_Dimension | list[E54_Dimension] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P43_has_dimension"})


class E71_Human_Made_Thing(E70_Thing):
    """Human-Made Thing <http://www.cidoc-crm.org/cidoc-crm/E71_Human-Made_Thing>.

    This class comprises discrete, identifiable human-made items that are documented as single units.
    These items are either intellectual products or human-made physical things, and are characterized by relative stability. They may for instance have a solid physical form, an electronic encoding, or they may be logical concepts or structures.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E71_Human-Made_Thing"
    P102_has_title: E35_Title | list[E35_Title] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P102_has_title"})
    P103_was_intended_for: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P103_was_intended_for"})
    P19i_was_made_for: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P19i_was_made_for"})


class E28_Conceptual_Object(E71_Human_Made_Thing):
    """Conceptual Object <http://www.cidoc-crm.org/cidoc-crm/E28_Conceptual_Object>.

    This class comprises non-material products of our minds and other human produced data that have become objects of a discourse about their identity, circumstances of creation or historical implication. The production of such information may have been supported by the use of technical devices such as cameras or computers.
    Characteristically, instances of this class are created, invented or thought by someone, and then may be documented or communicated between persons. Instances of E28 Conceptual Object have the ability to exist on more than one particular carrier at the same time, such as paper, electronic signals, marks, audio media, paintings, photos, human memories, etc.
    They cannot be destroyed. They exist as long as they can be found on at least one carrier or in at least one human memory. Their existence ends when the last carrier and the last memory are lost.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E28_Conceptual_Object"
    P94i_was_created_by: E65_Creation | list[E65_Creation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P94i_was_created_by"})


class E55_Type(E28_Conceptual_Object):
    """Type <http://www.cidoc-crm.org/cidoc-crm/E55_Type>.

    This class comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize and classify instances of CIDOC CRM classes. Instances of E55 Type represent concepts in contrast to instances of E41 Appellation which are used to name instances of CIDOC CRM classes.
    E55 Type is the CIDOC CRM’s interface to domain specific ontologies and thesauri. These can be represented in the CIDOC CRM as subclasses of E55 Type, forming hierarchies of terms, i.e., instances of E55 Type linked via P127 has broader term (has narrower term): E55 Type. Such hierarchies may be extended with additional properties.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E55_Type"
    P101i_was_use_of: E70_Thing | list[E70_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P101i_was_use_of"})
    P103i_was_intention_of: E71_Human_Made_Thing | list[E71_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P103i_was_intention_of"})
    P125i_was_type_of_object_used_in: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P125i_was_type_of_object_used_in"})
    P127_has_broader_term: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P127_has_broader_term"})
    P127i_has_narrower_term: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P127i_has_narrower_term"})
    P135i_was_created_by: E83_Type_Creation | list[E83_Type_Creation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P135i_was_created_by"})
    P137i_is_exemplified_by: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P137i_is_exemplified_by"})
    P150_defines_typical_parts_of: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P150_defines_typical_parts_of"})
    P150i_defines_typical_wholes_for: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P150i_defines_typical_wholes_for"})
    P177i_is_type_of_property_assigned: E13_Attribute_Assignment | list[E13_Attribute_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P177i_is_type_of_property_assigned"})
    P21i_was_purpose_of: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P21i_was_purpose_of"})
    P2i_is_type_of: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P2i_is_type_of"})
    P32i_was_technique_of: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P32i_was_technique_of"})
    P42i_was_assigned_by: E17_Type_Assignment | list[E17_Type_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P42i_was_assigned_by"})


class E56_Language(E55_Type):
    """Language <http://www.cidoc-crm.org/cidoc-crm/E56_Language>.

    This class is a specialization of E55 Type and comprises the natural languages in the sense of concepts.
    This type is used categorically in the model without reference to instances of it, i.e., the Model does not foresee the description of instances of instances of E56 Language, e.g.: “instances of Mandarin Chinese”.
    It is recommended that internationally or nationally agreed codes and terminology are used to denote instances of E56 Language, such as those defined in ISO 639-2:1998 and later versions.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E56_Language"
    P72i_is_language_of: E33_Linguistic_Object | list[E33_Linguistic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P72i_is_language_of"})


class E57_Material(E55_Type):
    """Material <http://www.cidoc-crm.org/cidoc-crm/E57_Material>.

    This class is a specialization of E55 Type and comprises the concepts of materials.
    Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing).
    This type is used categorically in the model without reference to instances of it, i.e., the Model does not foresee the description of instances of instances of E57 Material, e.g.: “instances of gold”.
    It is recommended that internationally or nationally agreed codes and terminology are used.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E57_Material"
    P126i_was_employed_in: E11_Modification | list[E11_Modification] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P126i_was_employed_in"})
    P45i_is_incorporated_in: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P45i_is_incorporated_in"})
    P68i_use_foreseen_by: E29_Design_or_Procedure | list[E29_Design_or_Procedure] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P68i_use_foreseen_by"})


class E58_Measurement_Unit(E55_Type):
    """Measurement Unit <http://www.cidoc-crm.org/cidoc-crm/E58_Measurement_Unit>.

    This class is a specialization of E55 Type and comprises the types of measurement units: feet, inches, centimetres, litres, lumens, etc.
    This type is used categorically in the model without reference to instances of it, i.e., the Model does not foresee the description of instances of instances of E58 Measurement Unit, e.g.: “instances of cm”.
    Système International (SI) units or internationally recognized non-SI terms should be used whenever possible, such as those defined by ISO80000:2009. Archaic Measurement Units used in historical records should be preserved.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E58_Measurement_Unit"
    P91i_is_unit_of: E54_Dimension | list[E54_Dimension] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P91i_is_unit_of"})


class E72_Legal_Object(E70_Thing):
    """Legal Object <http://www.cidoc-crm.org/cidoc-crm/E72_Legal_Object>.

    This class comprises those material or immaterial items to which instances of E30 Right, such as the right of ownership or use, can be applied.
    This is true for all instances of E18 Physical Thing. In the case of instances of E28 Conceptual Object, however, the identity of an instance of E28 Conceptual Object or the method of its use may be too ambiguous to reliably establish instances of E30 Right, as in the case of taxa and inspirations. Ownership of corporations is currently regarded as out of scope of the CIDOC CRM.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E72_Legal_Object"
    P104_is_subject_to: E30_Right | list[E30_Right] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P104_is_subject_to"})
    P105_right_held_by: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P105_right_held_by"})


class E18_Physical_Thing(E72_Legal_Object):
    """Physical Thing <http://www.cidoc-crm.org/cidoc-crm/E18_Physical_Thing>.

    This class comprises all persistent physical items with a relatively stable form, human-made or natural.
    Depending on the existence of natural boundaries of such things, the CIDOC CRM distinguishes the instances of E19 Physical Object from instances of E26 Physical Feature, such as holes, rivers, pieces of land etc. Most instances of E19 Physical Object can be moved (if not too heavy), whereas features are integral to the surrounding matter.
    An instance of E18 Physical Thing occupies not only a particular geometric space at any instant of its existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies a real, that is phenomenal, volume in spacetime. We include in the occupied space the space filled by the matter of the physical thing and all its inner spaces, such as the interior of a box. For the purpose of more detailed descriptions of the presence of an instance of E18 Physical Thing in space and time it can be associated with its specific instance of E92 Spacetime Volume by the property P196 defines (is defined by).
    The CIDOC CRM is generally not concerned with amounts of matter in fluid or gaseous states, as long as they are not confined in an identifiable way for an identifiable minimal time-span.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E18_Physical_Thing"
    P110i_was_augmented_by: E79_Part_Addition | list[E79_Part_Addition] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P110i_was_augmented_by"})
    P111i_was_added_by: E79_Part_Addition | list[E79_Part_Addition] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P111i_was_added_by"})
    P112i_was_diminished_by: E80_Part_Removal | list[E80_Part_Removal] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P112i_was_diminished_by"})
    P113i_was_removed_by: E80_Part_Removal | list[E80_Part_Removal] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P113i_was_removed_by"})
    P123i_resulted_from: E81_Transformation | list[E81_Transformation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P123i_resulted_from"})
    P124i_was_transformed_by: E81_Transformation | list[E81_Transformation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P124i_was_transformed_by"})
    P128_carries: E90_Symbolic_Object | list[E90_Symbolic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P128_carries"})
    P13i_was_destroyed_by: E6_Destruction | list[E6_Destruction] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P13i_was_destroyed_by"})
    P156_occupies: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P156_occupies"})
    P157i_provides_reference_space_for: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P157i_provides_reference_space_for"})
    P195i_had_presence: E93_Presence | list[E93_Presence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P195i_had_presence"})
    P196_defines: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P196_defines"})
    P198_holds_or_supports: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P198_holds_or_supports"})
    P198i_is_held_or_supported_by: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P198i_is_held_or_supported_by"})
    P24i_changed_ownership_through: E8_Acquisition | list[E8_Acquisition] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P24i_changed_ownership_through"})
    P30i_custody_transferred_through: E10_Transfer_of_Custody | list[E10_Transfer_of_Custody] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P30i_custody_transferred_through"})
    P31i_was_modified_by: E11_Modification | list[E11_Modification] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P31i_was_modified_by"})
    P34i_was_assessed_by: E14_Condition_Assessment | list[E14_Condition_Assessment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P34i_was_assessed_by"})
    P39i_was_measured_by: E16_Measurement | list[E16_Measurement] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P39i_was_measured_by"})
    P44_has_condition: E3_Condition_State | list[E3_Condition_State] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P44_has_condition"})
    P45_consists_of: E57_Material | list[E57_Material] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P45_consists_of"})
    P46_is_composed_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P46_is_composed_of"})
    P46i_forms_part_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P46i_forms_part_of"})
    P49_has_former_or_current_keeper: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P49_has_former_or_current_keeper"})
    P50_has_current_keeper: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P50_has_current_keeper"})
    P51_has_former_or_current_owner: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P51_has_former_or_current_owner"})
    P52_has_current_owner: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P52_has_current_owner"})
    P53_has_former_or_current_location: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P53_has_former_or_current_location"})
    P59_has_section: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P59_has_section"})
    P8i_witnessed: E4_Period | list[E4_Period] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P8i_witnessed"})


class E19_Physical_Object(E18_Physical_Thing):
    """Physical Object <http://www.cidoc-crm.org/cidoc-crm/E19_Physical_Object>.

    This class comprises items of a material nature that are units for documentation and have physical boundaries that separate them completely in an objective way from other objects.
    The class also includes all aggregates of objects made for functional purposes of whatever kind, independent of physical coherence, such as a set of chessmen. Typically, instances of E19 Physical Object can be moved (if not too heavy).
    In some contexts, such objects, except for aggregates, are also called “bona fide objects” (Smith &amp; Varzi, 2000, pp.401-420), i.e., naturally defined objects.
    The decision as to what is documented as a complete item, rather than by its parts or components, may be a purely administrative decision or may be a result of the order in which the item was acquired.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E19_Physical_Object"
    P188i_is_production_tool_for: E99_Product_Type | list[E99_Product_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P188i_is_production_tool_for"})
    P25i_moved_by: E9_Move | list[E9_Move] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P25i_moved_by"})
    P54_has_current_permanent_location: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P54_has_current_permanent_location"})
    P55_has_current_location: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P55_has_current_location"})
    P56_bears_feature: E26_Physical_Feature | list[E26_Physical_Feature] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P56_bears_feature"})
    P57_has_number_of_parts: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P57_has_number_of_parts"})


class E20_Biological_Object(E19_Physical_Object):
    """Biological Object <http://www.cidoc-crm.org/cidoc-crm/E20_Biological_Object>.

    This class comprises individual items of a material nature, which live, have lived or are natural products of or from living organisms.
    Artificial objects that incorporate biological elements, such as Victorian butterfly frames, can be documented as both instances of E20 Biological Object and E22 Human-Made Object.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E20_Biological_Object"
    ...


class E21_Person(E20_Biological_Object, E39_Actor):
    """Person <http://www.cidoc-crm.org/cidoc-crm/E21_Person>.

    This class comprises real persons who live or are assumed to have lived.
    Legendary figures that may have existed, such as Ulysses and King Arthur, fall into this class if the documentation refers to them as historical figures. In cases where doubt exists as to whether several persons are in fact identical, multiple instances can be created and linked to indicate their relationship. The CIDOC CRM does not propose a specific form to support reasoning about possible identity.
    In a bibliographic context, a name presented following the conventions usually employed for personal names will be assumed to correspond to an actual real person (an instance of E21 Person), unless evidence is available to indicate that this is not the case. The fact that a persona may erroneously be classified as an instance of E21 Person does not imply that the concept comprises personae.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E21_Person"
    P100i_died_in: E69_Death | list[E69_Death] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P100i_died_in"})
    P152_has_parent: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P152_has_parent"})
    P152i_is_parent_of: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P152i_is_parent_of"})
    P96i_gave_birth: E67_Birth | list[E67_Birth] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P96i_gave_birth"})
    P97i_was_father_for: E67_Birth | list[E67_Birth] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P97i_was_father_for"})
    P98i_was_born: E67_Birth | list[E67_Birth] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P98i_was_born"})


class E24_Physical_Human_Made_Thing(E18_Physical_Thing, E71_Human_Made_Thing):
    """Physical Human-Made Thing <http://www.cidoc-crm.org/cidoc-crm/E24_Physical_Human-Made_Thing>.

    This class comprises all persistent physical items of any size that are purposely created by human activity. This class comprises, besides others, Human-Made objects, such as a sword, and Human-Made features, such as rock art. For example, a “cup and ring” carving on bedrock is regarded as instance of E24 Physical Human-Made Thing.
    Instances of Human-Made thing may be the result of modifying pre-existing physical things, preserving larger parts or most of the original matter and structure, which poses the question if they are new or even Human-Made, the respective interventions of production made on such original material should be obvious and sufficient to regard that the product has a new, distinct identity and intended function and is human-made. Substantial continuity of the previous matter and structure in the new product can be documented by describing the production process also as an instance of E81 Transformation.
    Whereas interventions of conservation and repair are not regarded to produce a new Human-Made thing, the results of preparation of natural history specimens that substantially change their natural or original state should be regarded as physical Human-Made things, including the uncovering of petrified biological features from a solid piece of stone. On the other side, scribbling a museum number on a natural object should not be regarded to make it Human-Made. This notwithstanding, parts, sections, segments, or features of a physical Human-Made thing may continue to be non-Human-Made and preserved during the production process, for example natural pearls used as a part of an eardrop.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E24_Physical_Human-Made_Thing"
    P108i_was_produced_by: E12_Production | list[E12_Production] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P108i_was_produced_by"})
    P62_depicts: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P62_depicts"})
    P65_shows_visual_item: E36_Visual_Item | list[E36_Visual_Item] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P65_shows_visual_item"})


class E22_Human_Made_Object(E19_Physical_Object, E24_Physical_Human_Made_Thing):
    """Human-Made Object <http://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object>.

    This class comprises all persistent physical objects of any size that are purposely created by human activity and have physical boundaries that separate them completely in an objective way from other objects.
    The class also includes all aggregates of objects made for functional purposes of whatever kind, independent of physical coherence, such as a set of chessmen.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object"
    ...


class E26_Physical_Feature(E18_Physical_Thing):
    """Physical Feature <http://www.cidoc-crm.org/cidoc-crm/E26_Physical_Feature>.

    This class comprises identifiable features that are physically attached in an integral way to particular physical objects.
    Instances of E26 Physical Feature share many of the attributes of instances of E19 Physical Object. They may have a one-, two- or three-dimensional geometric extent, but there are no natural borders that separate them completely in an objective way from the carrier objects. For example, a doorway is a feature but the door itself, being attached by hinges, is not.
    Instances of E26 Physical Feature can be features in a narrower sense, such as scratches, holes, reliefs, surface colours, reflection zones in an opal crystal or a density change in a piece of wood. In the wider sense, they are portions of particular objects with partially imaginary borders, such as the core of the Earth, an area of property on the surface of the Earth, a landscape or the head of a contiguous marble statue. They can be measured and dated, and it is sometimes possible to state who or what is or was responsible for them. They cannot be separated from the carrier object, but a segment of the carrier object may be identified (or sometimes removed) carrying the complete feature.
    This definition coincides with the definition of "fiat objects" (Smith &amp; Varzi, 2000, pp.401-420), with the exception of aggregates of “bona fide objects”.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E26_Physical_Feature"
    P56i_is_found_on: E19_Physical_Object | list[E19_Physical_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P56i_is_found_on"})


class E25_Human_Made_Feature(E24_Physical_Human_Made_Thing, E26_Physical_Feature):
    """Human-Made Feature <http://www.cidoc-crm.org/cidoc-crm/E25_Human-Made_Feature>.

    This class comprises physical features that are purposely created by human activity, such as scratches, artificial caves, artificial water channels, etc. In particular, it includes the information encoding features on mechanical or digital carriers.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E25_Human-Made_Feature"
    ...


class E27_Site(E26_Physical_Feature):
    """Site <http://www.cidoc-crm.org/cidoc-crm/E27_Site>.

    This class comprises pieces of land or sea floor.
    In contrast to the purely geometric notion of E53 Place, this class describes constellations of matter on the surface of the Earth or other celestial body, which can be represented by photographs, paintings and maps.
    Instances of E27 Site are composed of relatively immobile material items and features in a particular configuration at a particular location.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E27_Site"
    ...


class E74_Group(E39_Actor):
    """Group <http://www.cidoc-crm.org/cidoc-crm/E74_Group>.

    This class comprises any gatherings or organizations of human individuals or groups that act collectively or in a similar way due to any form of unifying relationship. In the wider sense this class also comprises official positions which used to be regarded in certain contexts as one actor, independent of the current holder of the office, such as the president of a country. In such cases, it may happen that the group never had more than one member. A joint pseudonym (i.e., a name that seems indicative of an individual but that is actually used as a persona by two or more people) is a particular case of E74 Group.
    A gathering of people becomes an instance of E74 Group when it exhibits organizational characteristics usually typified by a set of ideas or beliefs held in common, or actions performed together. These might be communication, creating some common artifact, a common purpose such as study, worship, business, sports, etc. Nationality can be modelled as membership in an instance of E74 Group. Married couples and other concepts of family are regarded as particular examples of E74 Group.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E74_Group"
    P107_has_current_or_former_member: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P107_has_current_or_former_member"})
    P144i_gained_member_by: E85_Joining | list[E85_Joining] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P144i_gained_member_by"})
    P146i_lost_member_by: E86_Leaving | list[E86_Leaving] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P146i_lost_member_by"})
    P151i_participated_in: E66_Formation | list[E66_Formation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P151i_participated_in"})
    P95i_was_formed_by: E66_Formation | list[E66_Formation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P95i_was_formed_by"})
    P99i_was_dissolved_by: E68_Dissolution | list[E68_Dissolution] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P99i_was_dissolved_by"})


class E78_Curated_Holding(E24_Physical_Human_Made_Thing):
    """Curated Holding <http://www.cidoc-crm.org/cidoc-crm/E78_Curated_Holding>.

    This class comprises aggregations of instances of E18 Physical Thing that are assembled and maintained (“curated” and “preserved,” in museological terminology) by one or more instances of E39 Actor over time for a specific purpose and audience, and according to a particular collection development plan. Typical instances of curated holdings are museum collections, archives, library holdings and digital libraries. A digital library is regarded as an instance of E18 Physical Thing because it requires keeping physical carriers of the electronic content.
    Items may be added or removed from an E78 Curated Holding in pursuit of this plan. This class should not be confused with the E39 Actor maintaining the E78 Curated Holding often referred to with the name of the E78 Curated Holding (e.g., “The Wallace Collection decided…”).
    Collective objects in the general sense, like a tomb full of gifts, a folder with stamps or a set of chessmen, should be documented as instances of E19 Physical Object, and not as instances of E78 Curated Holding. This is because they form wholes either because they are physically bound together or because they are kept together for their functionality.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E78_Curated_Holding"
    P109_has_current_or_former_curator: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P109_has_current_or_former_curator"})
    P147i_was_curated_by: E87_Curation_Activity | list[E87_Curation_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P147i_was_curated_by"})


class E89_Propositional_Object(E28_Conceptual_Object):
    """Propositional Object <http://www.cidoc-crm.org/cidoc-crm/E89_Propositional_Object>.

    This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions, algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real or imaginary things and that are documented as single units or serve as topic of discourse.
    This class also comprises items that are “about” something in the sense of a subject. In the wider sense, this class includes expressions of psychological value such as non-figural art and musical themes. However, conceptual items such as types and classes are not instances of E89 Propositional Object. This should not be confused with the definition of a type, which is indeed an instance of E89 Propositional Object.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E89_Propositional_Object"
    P129_is_about: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P129_is_about"})
    P148_has_component: E89_Propositional_Object | list[E89_Propositional_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P148_has_component"})
    P148i_is_component_of: E89_Propositional_Object | list[E89_Propositional_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P148i_is_component_of"})
    P67_refers_to: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P67_refers_to"})


class E30_Right(E89_Propositional_Object):
    """Right <http://www.cidoc-crm.org/cidoc-crm/E30_Right>.

    This class comprises legal privileges concerning material and immaterial things or their derivatives.
    These include reproduction and property rights.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E30_Right"
    P104i_applies_to: E72_Legal_Object | list[E72_Legal_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P104i_applies_to"})
    P75i_is_possessed_by: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P75i_is_possessed_by"})


class E90_Symbolic_Object(E28_Conceptual_Object, E72_Legal_Object):
    """Symbolic Object <http://www.cidoc-crm.org/cidoc-crm/E90_Symbolic_Object>.

    This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers, traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code or mathematical formulae that have an objectively recognizable structure and that are documented as single units.
    It includes sets of signs of any nature, which may serve to designate something, or to communicate some propositional content. An instance of E90 Symbolic Object may or may not have a specific meaning, for example an arbitrary character string.
    In some cases, the content of an instance of E90 Symbolic Object may completely be represented by a serialized digital content model, such as a sequence of ASCII-encoded characters, an XML or HTML document, or a TIFF image. The property P3 has note and its subproperty P190 has symbolic content allow for the description of this content model. In order to disambiguate which symbolic level is the carrier of the meaning, the property P3.1 has type can be used to specify the encoding (e.g., "bit", "Latin character", RGB pixel).
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E90_Symbolic_Object"
    P106_is_composed_of: E90_Symbolic_Object | list[E90_Symbolic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P106_is_composed_of"})
    P106i_forms_part_of: E90_Symbolic_Object | list[E90_Symbolic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P106i_forms_part_of"})
    P128i_is_carried_by: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P128i_is_carried_by"})
    P142i_was_used_in: E15_Identifier_Assignment | list[E15_Identifier_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P142i_was_used_in"})
    P165i_is_incorporated_in: E73_Information_Object | list[E73_Information_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P165i_is_incorporated_in"})
    P190_has_symbolic_content: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P190_has_symbolic_content"})


class E41_Appellation(E90_Symbolic_Object):
    """Appellation <http://www.cidoc-crm.org/cidoc-crm/E41_Appellation>.

    This class comprises signs, either meaningful or not, or arrangements of signs following a specific syntax, that are used or can be used to refer to and identify a specific instance of some class or category within a certain context.
    Instances of E41 Appellation do not identify things by their meaning, even if they happen to have one, but instead by convention, tradition, or agreement. Instances of E41 Appellation are cultural constructs; as such, they have a context, a history, and a use in time and space by some group of users. A given instance of E41 Appellation can have alternative forms, i.e., other instances of E41 Appellation that are always regarded as equivalent independent from the thing it denotes.
    Different languages may use different appellations for the same thing, such as the names of major cities. Some appellations may be formulated using a valid noun phrase of a particular language. In these cases, the respective instances of E41 Appellation should also be declared as instances of E33 Linguistic Object. Then the language using the appellation can be declared with the property P72 has language: E56 Language.
    Instances of E41 Appellation may be used to identify any instance of E1 CRM Entity and sometimes are characteristic for instances of more specific subclasses E1 CRM Entity, such as for instances of E52 Time-Span (for instance “dates”), E39 Actor, E53 Place or E28 Conceptual Object. Postal addresses and E-mail addresses are characteristic examples of identifiers used by services transporting things between clients.
    Even numerically expressed identifiers for extents in space or time are also regarded as instances of E41 Appellation, such as Gregorian dates or spatial coordinates, even though they allow for determining some time or location by a known procedure starting from a reference point and by virtue of that fact play a double role as instances of E59 Primitive Value.
    E41 Appellation should not be confused with the act of naming something. Cf. E15 Identifier Assignment.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E41_Appellation"
    P139_has_alternative_form: E41_Appellation | list[E41_Appellation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P139_has_alternative_form"})
    P139i_is_alternative_form_of: E41_Appellation | list[E41_Appellation] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P139i_is_alternative_form_of"})
    P1i_identifies: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P1i_identifies"})
    P76i_provides_access_to: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P76i_provides_access_to"})


class E42_Identifier(E41_Appellation):
    """Identifier <http://www.cidoc-crm.org/cidoc-crm/E42_Identifier>.

    This class comprises strings or codes assigned to instances of E1 CRM Entity in order to identify them uniquely and permanently within the context of one or more organisations. Such codes are often known as inventory numbers, registration codes, etc. and are typically composed of alphanumeric sequences. Postal addresses, telephone numbers, URLs and e-mail addresses are characteristic examples of identifiers used by services transporting things between clients.
    The class E42 Identifier is not normally used for machine-generated identifiers used for automated processing unless these are also used by human agents.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E42_Identifier"
    P37i_was_assigned_by: E15_Identifier_Assignment | list[E15_Identifier_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P37i_was_assigned_by"})
    P38i_was_deassigned_by: E15_Identifier_Assignment | list[E15_Identifier_Assignment] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P38i_was_deassigned_by"})
    P48i_is_preferred_identifier_of: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P48i_is_preferred_identifier_of"})


class E73_Information_Object(E89_Propositional_Object, E90_Symbolic_Object):
    """Information Object <http://www.cidoc-crm.org/cidoc-crm/E73_Information_Object>.

    This class comprises identifiable immaterial items, such as poems, jokes, data sets, images, texts, multimedia objects, procedural prescriptions, computer program code, algorithm or mathematical formulae, that have an objectively recognizable structure and are documented as single units. The encoding structure known as a "named graph" also falls under this class, so that each "named graph" is an instance of E73 Information Object.
    An instance of E73 Information Object does not depend on a specific physical carrier, which can include human memory, and it can exist on one or more carriers simultaneously.
    Instances of E73 Information Object of a linguistic nature should be declared as instances of the E33 Linguistic Object subclass. Instances of E73 Information Object of a documentary nature should be declared as instances of the E31 Document subclass. Conceptual items such as types and classes are not instances of E73 Information Object, nor are ideas without a reproducible expression.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E73_Information_Object"
    P165_incorporates: E90_Symbolic_Object | list[E90_Symbolic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P165_incorporates"})


class E29_Design_or_Procedure(E73_Information_Object):
    """Design or Procedure <http://www.cidoc-crm.org/cidoc-crm/E29_Design_or_Procedure>.

    This class comprises documented plans for the execution of actions in order to achieve a result of a specific quality, form or contents. In particular, it comprises plans for deliberate human activities that may result in new instances of E71 Human-Made Thing or for shaping or guiding the execution of an instance of E7 Activity.
    Instances of E29 Design or Procedure can be structured in parts and sequences or depend on others.
    This is modelled using P69 has association with (is associated with): E29 Design or Procedure.
    Designs or procedures can be seen as one of the following.
    1. A schema for the activities it describes.
    2. A schema of the products that result from their application.
    3. An independent intellectual product that may have never been applied, such as Leonardo da Vinci’s famous plans for flying machines.
    Because designs or procedures may never be applied or only partially executed, the CIDOC CRM models a loose relationship between the plan and the respective product.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E29_Design_or_Procedure"
    P187i_is_production_plan_for: E99_Product_Type | list[E99_Product_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P187i_is_production_plan_for"})
    P33i_was_used_by: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P33i_was_used_by"})
    P68_foresees_use_of: E57_Material | list[E57_Material] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P68_foresees_use_of"})
    P69_has_association_with: E29_Design_or_Procedure | list[E29_Design_or_Procedure] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P69_has_association_with"})
    P69i_is_associated_with: E29_Design_or_Procedure | list[E29_Design_or_Procedure] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P69i_is_associated_with"})


class E31_Document(E73_Information_Object):
    """Document <http://www.cidoc-crm.org/cidoc-crm/E31_Document>.

    This class comprises identifiable immaterial items that make propositions about reality.
    These propositions may be expressed in text, graphics, images, audiograms, videograms or by other similar means. Documentation databases are regarded as instances of E31 Document. This class should not be confused with the concept “document” in Information Technology, which is compatible with E73 Information Object.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E31_Document"
    P70_documents: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P70_documents"})


class E32_Authority_Document(E31_Document):
    """Authority Document <http://www.cidoc-crm.org/cidoc-crm/E32_Authority_Document>.

    This class comprises encyclopaedia, thesauri, authority lists and other documents that define terminology or conceptual systems for consistent use.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E32_Authority_Document"
    P71_lists: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P71_lists"})


class E33_Linguistic_Object(E73_Information_Object):
    """Linguistic Object <http://www.cidoc-crm.org/cidoc-crm/E33_Linguistic_Object>.

    This class comprises identifiable expressions in natural language or languages.
    Instances of E33 Linguistic Object can be expressed in many ways: e.g., as written texts, recorded speech or sign language. However, the CIDOC CRM treats instances of E33 Linguistic Object independently from the medium or method by which they are expressed. Expressions in formal languages, such as computer code or mathematical formulae, are not treated as instances of E33 Linguistic Object by the CIDOC CRM. These should be modelled as instances of E73 Information Object.
    In general, an instance of E33 Linguistic Object may also contain non-linguistic information, often of artistic or aesthetic value. Only in cases in which the content of an instance of E33 Linguistic Object can completely be expressed by a series of binary-encoded symbols, its content may be documented within a respective knowledge base by the property P190 has symbolic content: E62 String. Otherwise, it should be understood as an identifiable digital resource only available independently from the respective knowledge base.
    In other cases, such as pages of an illuminated manuscript or recordings containing speech in a language supported by a writing system, the linguistic part of the content of an instance of E33 Linguistic Object may be documented within a respective knowledge base in a note by P3 has note: E62 String. Otherwise, it may be described using the property P165 incorporates (is incorporated in): E73 Information Object as a different object with its own identity.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E33_Linguistic_Object"
    P72_has_language: E56_Language | list[E56_Language] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P72_has_language"})
    P73_has_translation: E33_Linguistic_Object | list[E33_Linguistic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P73_has_translation"})
    P73i_is_translation_of: E33_Linguistic_Object | list[E33_Linguistic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P73i_is_translation_of"})


class E33_E41_Linguistic_Appellation(E33_Linguistic_Object, E41_Appellation):
    """Linguistic Appellation <http://www.cidoc-crm.org/cidoc-crm/E33_E41_Linguistic_Appellation>."""
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E33_E41_Linguistic_Appellation"
    ...


class E35_Title(E33_Linguistic_Object, E41_Appellation):
    """Title <http://www.cidoc-crm.org/cidoc-crm/E35_Title>.

    This class comprises textual strings that within a cultural context can be clearly identified as titles due to their form. Being a subclass of E41 Appellation, E35 Title can only be used when such a string is actually used as a title of a work, such as a text, an artwork, or a piece of music.
    Titles are proper noun phrases or verbal phrases, and should not be confused with generic object names such as “chair”, “painting” or “book” (the latter are common nouns that stand for instances of E55 Type). Titles may be assigned by the creator of the work itself, or by a social group.
    This class also comprises the translations of titles that are used as surrogates for the original titles in different social contexts.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E35_Title"
    P102i_is_title_of: E71_Human_Made_Thing | list[E71_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P102i_is_title_of"})


class E36_Visual_Item(E73_Information_Object):
    """Visual Item <http://www.cidoc-crm.org/cidoc-crm/E36_Visual_Item>.

    This class comprises the intellectual or conceptual aspects of recognisable marks, images and other visual works.
    This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment of a visual item, but the underlying prototype. For example, a mark such as the ICOM logo is generally considered to be the same logo when used on any number of publications. The size, orientation and colour may change, but the logo remains uniquely identifiable. The same is true of images that are reproduced many times. This means that visual items are independent of their physical support.
    The class E36 Visual Item provides a means of identifying and linking together instances of E24 Physical Human-Made Thing that carry the same visual qualities (symbols, marks or images etc.). The property P62 depicts (is depicted by) between E24 Physical Human-Made Thing and depicted subjects (E1 CRM Entity) is a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65 shows visual item (is shown by), E36 Visual Item, P138 represents (has representation) to E1CRM Entity, which in addition captures the optical features of the depiction.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E36_Visual_Item"
    P138_represents: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P138_represents"})
    P65i_is_shown_by: E24_Physical_Human_Made_Thing | list[E24_Physical_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P65i_is_shown_by"})


class E37_Mark(E36_Visual_Item):
    """Mark <http://www.cidoc-crm.org/cidoc-crm/E37_Mark>.

    This class comprises symbols, signs, signatures or short texts applied to instances of E24 Physical Human-Made Thing by arbitrary techniques, often in order to indicate such things as creator, owner, dedications, purpose or to communicate information generally. Instances of E37 Mark do not represent the actual image of a mark, but the abstract ideal (or archetype) as used for codification in reference documents forming cultural documentation.
    This class specifically excludes features that have no semantic significance, such as scratches or tool marks. These should be documented as instances of E25 Human-Made Feature.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E37_Mark"
    ...


class E34_Inscription(E33_Linguistic_Object, E37_Mark):
    """Inscription <http://www.cidoc-crm.org/cidoc-crm/E34_Inscription>.

    This class comprises recognisable, texts attached to instances of E24 Physical Human-Made Thing.
    The transcription of the text can be documented in a note by P3 has note: E62 String. The alphabet used can be documented by P2 has type: E55 Type. This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment of an inscription, but the underlying prototype. The physical embodiment is modelled in the CIDOC CRM as instances of E24 Physical Human-Made Thing.
    The relationship of a physical copy of a book to the text it contains is modelled using E18 Physical Thing. P128 carries (is carried by): E33 Linguistic Object.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E34_Inscription"
    ...


class E92_Spacetime_Volume(E1_CRM_Entity):
    """Spacetime Volume <http://www.cidoc-crm.org/cidoc-crm/E92_Spacetime_Volume>.

    This class comprises 4-dimensional point sets (volumes) in physical spacetime (in contrast to mathematical models of it) regardless their true geometric forms. They may derive their identity from being the extent of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime. Intersections of instances of E92 Spacetime Volume, E53 Place and E52 Time-Span are also regarded as instances of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives from or due to the limited precision up to which defining expression can be identified with a real extent in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E92_Spacetime_Volume"
    P10_falls_within: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P10_falls_within"})
    P10i_contains: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P10i_contains"})
    P132_spatiotemporally_overlaps_with: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P132_spatiotemporally_overlaps_with"})
    P133_is_spatiotemporally_separated_from: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P133_is_spatiotemporally_separated_from"})
    P160_has_temporal_projection: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P160_has_temporal_projection"})
    P161_has_spatial_projection: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P161_has_spatial_projection"})
    P166i_had_presence: E93_Presence | list[E93_Presence] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P166i_had_presence"})
    P169i_spacetime_volume_is_defined_by: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P169i_spacetime_volume_is_defined_by"})
    P196i_is_defined_by: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P196i_is_defined_by"})


class E4_Period(E2_Temporal_Entity, E92_Spacetime_Volume):
    """Period <http://www.cidoc-crm.org/cidoc-crm/E4_Period>.

    This class comprises sets of coherent phenomena or cultural manifestations occurring in time and space.
    It is the social or physical coherence of these phenomena that identify an instance of E4 Period and not the associated spatiotemporal extent. This extent is only the “ground” or space in an abstract physical sense that the actual process of growth, spread and retreat has covered. Consequently, different periods can overlap and coexist in time and space, such as when a nomadic culture exists in the same area and time as a sedentary culture. This also means that overlapping land use rights, common among first nations, amounts to overlapping periods.
    Often, this class is used to describe prehistoric or historic periods such as the “Neolithic Period”, the “Ming Dynasty” or the “McCarthy Era”, but also geopolitical units and activities of settlements are regarded as special cases of E4 Period. However, there are no assumptions about the scale of the associated phenomena. In particular all events are seen as synthetic processes consisting of coherent phenomena. Therefore, E4 Period is a superclass of E5 Event. For example, a modern clinical birth, an instance of E67 Birth, can be seen as both a single event, i.e., an instance of E5 Event, and as an extended period, i.e., an instance of E4 Period, that consists of multiple physical processes and complementary activities performed by multiple instances of E39 Actor.
    As the actual extent of an instance of E4 Period in spacetime we regard the trajectories of the participating physical things during their participation in an instance of E4 Period. This includes the open spaces via which these things have interacted and the spaces by which they had the potential to interact during that period or event in the way defined by the type of the respective period or event. Examples include the air in a meeting room transferring the voices of the participants. Since these phenomena are fuzzy, we assume the spatiotemporal extent to be contiguous, except for cases of phenomena spreading out over islands or other separated areas, including geopolitical units distributed over disconnected areas such as islands or colonies.
    Whether the trajectories necessary for participants to travel between these areas are regarded as part of the spatiotemporal extent or not has to be decided in each case based on a concrete analysis, taking use of the sea for other purposes than travel, such as fishing, into consideration. One may also argue that the activities to govern disconnected areas imply travelling through spaces connecting them and that these areas hence are spatially connected in a way, but it appears counterintuitive to consider for instance travel routes in international waters as extensions of geopolitical units.
    Consequently, an instance of E4 Period may occupy a number of disjoint spacetime volumes, however there must not be a discontinuity in the time-span covered by these spacetime volumes. This means that an instance of E4 Period must be contiguous in time. If it has ended in all areas, it has ended as a whole. However, it may end in one area before another, such as in the Polynesian migration, and it continues as long as it is ongoing in at least one area.
    We model E4 Period as a subclass of E2 Temporal Entity and of E92 Spacetime Volume. The latter is intended as a phenomenal spacetime volume as defined in CIDOC CRMgeo (Doerr &amp; Hiebel, 2013). By virtue of this multiple inheritance, we can discuss the physical extent of an instance of E4 Period without representing each instance of it together with an instance of its associated spacetime volume. This model combines two quite different kinds of substance: an instance of E4 Period is a phenomenon while an instance of E92 Spacetime Volume is an aggregation of points in spacetime. However, the real spatiotemporal extent of an instance of E4 Period is regarded to be unique to it due to all its details and fuzziness; its identity and existence depends uniquely on the identity of the instance of E4 Period. Therefore, this multiple inheritance is unambiguous and effective and furthermore corresponds to the intuitions of natural language.
    Typical use of this class in cultural heritage documentation is for documenting cultural and artistic periods. There are two different conceptualisations of ‘artistic style’, defined either by physical features or by historical context. For example, “Impressionism” can be viewed as a period in the European sphere of influence lasting from approximately 1870 to 1905 during which paintings with particular characteristics were produced by a group of artists that included (among others) Monet, Renoir, Pissarro, Sisley and Degas. Alternatively, it can be regarded as a style applicable to all paintings sharing the characteristics of the works produced by the Impressionist painters, regardless of historical context. The first interpretation is an instance of E4 Period, and the second defines morphological object types that fall under E55 Type.
    A geopolitical unit as a specific case of an instance of E4 Period is the set of activities and phenomena related to the claim of power, the consequences of belonging to a jurisdictional area and an administrative system that establishes a geopolitical unit. Examples from the modern period are countries or administrative areas of countries such as districts whose actions and structures define activities and phenomena in the area that they intend to govern. The borders of geopolitical units are often defined in contracts or treaties although they may deviate from the actual practice. The spatiotemporal properties of Geopolitical units can be modelled through the properties inherited from E92 Spacetime Volume.
    Another specific case of an instance of E4 Period is the actual extent of the set of activities and phenomena as evidenced by their physical traces that define a settlement, such as the populated period of Nineveh.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E4_Period"
    P7_took_place_at: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P7_took_place_at"})
    P8_took_place_on_or_within: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P8_took_place_on_or_within"})
    P9_consists_of: E4_Period | list[E4_Period] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P9_consists_of"})
    P9i_forms_part_of: E4_Period | list[E4_Period] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P9i_forms_part_of"})


class E5_Event(E4_Period):
    """Event <http://www.cidoc-crm.org/cidoc-crm/E5_Event>.

    This class comprises distinct, delimited and coherent processes and interactions of a material nature, in cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way characteristic of the kind of process. Typical examples are meetings, births, deaths, actions of decision taking, making or inventing things, but also more complex and extended ones such as conferences, elections, building of a castle, or battles.
    While the continuous growth of a tree lacks the limits characteristic of an event, its germination from a seed does qualify as an event. Similarly, the blowing of the wind lacks the distinctness and limits of an event, but a hurricane, flood or earthquake would qualify as an event. Mental processes are considered as events, in cases where they are connected with the material externalization of their results; for example, the creation of a poem, a performance or a change of intention that becomes obvious from subsequent actions or declarations.
    The effects of an instance of E5 Event may not lead to relevant permanent changes of properties or relations of the items involved in it, for example an unrecorded performance. Of course, in order to be documented, some kind of evidence for an event must exist, be it witnesses, traces or products of the event.
    While instances of E4 Period always require some form of coherence between its constituent phenomena, in addition, the essential constituents of instances of E5 Event should contribute to an overall effect; for example, the statements made during a meeting and the listening of the audience.
    Viewed at a coarse level of detail, an instance of E5 Event may appear as if it had an ‘instantaneous’ overall effect, but any process or interaction of material nature in reality have an extent in time and space. At a fine level, instances of E5 Event may be analysed into component phenomena and phases within a space and timeframe, and as such can be seen as a period, regardless of the size of the phenomena. The reverse is not necessarily the case: not all instances of E4 Period give rise to a noteworthy overall effect and are thus not instances of E5 Event.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E5_Event"
    P11_had_participant: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P11_had_participant"})
    P12_occurred_in_the_presence_of: E77_Persistent_Item | list[E77_Persistent_Item] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P12_occurred_in_the_presence_of"})
    P20i_was_purpose_of: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P20i_was_purpose_of"})


class E63_Beginning_of_Existence(E5_Event):
    """Beginning of Existence <http://www.cidoc-crm.org/cidoc-crm/E63_Beginning_of_Existence>.

    This class comprises events that bring into existence any instance of E77 Persistent Item.
    It may be used for temporal reasoning about things (intellectual products, physical items, groups of people, living beings) beginning to exist; it serves as a hook for determination of a “terminus post quem” or “terminus ante quem”.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E63_Beginning_of_Existence"
    P92_brought_into_existence: E77_Persistent_Item | list[E77_Persistent_Item] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P92_brought_into_existence"})


class E64_End_of_Existence(E5_Event):
    """End of Existence <http://www.cidoc-crm.org/cidoc-crm/E64_End_of_Existence>.

    This class comprises events that end the existence of any instance of E77 Persistent Item.
    It may be used for temporal reasoning about things (physical items, groups of people, living beings) ceasing to exist; it serves as a hook for determination of a “terminus post quem” or “terminus ante quem”. In cases where substance from an instance of E77 Persistent Item continues to exist in a new form, the process would be documented as instances of E81 Transformation.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E64_End_of_Existence"
    P93_took_out_of_existence: E77_Persistent_Item | list[E77_Persistent_Item] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P93_took_out_of_existence"})


class E67_Birth(E63_Beginning_of_Existence):
    """Birth <http://www.cidoc-crm.org/cidoc-crm/E67_Birth>.

    This class comprises the births of human beings. E67 Birth is a biological event focussing on the context of people coming into life. (E63 Beginning of Existence comprises the coming into life of any living being).
    Twins, triplets etc. are typically brought into life by the same instance of E67 Birth. The introduction of E67 Birth as a documentation element allows the description of a range of family relationships in a simple model. Suitable extensions may describe more details and the complexity of motherhood with the intervention of modern medicine. In this model, the biological father is not seen as a necessary participant in the birth.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E67_Birth"
    P96_by_mother: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P96_by_mother"})
    P97_from_father: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P97_from_father"})
    P98_brought_into_life: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P98_brought_into_life"})


class E68_Dissolution(E64_End_of_Existence):
    """Dissolution <http://www.cidoc-crm.org/cidoc-crm/E68_Dissolution>.

    This class comprises the events that result in the formal or informal termination of an instance of E74 Group.
    If the dissolution was deliberate, the Dissolution event should also be instantiated as an instance of E7 Activity.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E68_Dissolution"
    P99_dissolved: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P99_dissolved"})


class E69_Death(E64_End_of_Existence):
    """Death <http://www.cidoc-crm.org/cidoc-crm/E69_Death>.

    This class comprises the deaths of human beings.
    If a person is killed, the death should be documented as an instance of both E69 Death and E7 Activity. The death or perishing of other living beings should be documented as instances of E64 End of Existence.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E69_Death"
    P100_was_death_of: E21_Person | list[E21_Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P100_was_death_of"})


class E6_Destruction(E64_End_of_Existence):
    """Destruction <http://www.cidoc-crm.org/cidoc-crm/E6_Destruction>.

    This class comprises events that destroy one or more instances of E18 Physical Thing such that they lose their identity as the subjects of documentation.
    Some destruction events are intentional, while others are independent of human activity. Intentional destruction may be documented by classifying the event as both an instance of E6 Destruction and of E7 Activity.
    The decision to document an object as destroyed, transformed or modified is context sensitive:.
    1. If the matter remaining from the destruction is not documented, the event is modelled solely as an instance of E6 Destruction.
    2. An event should also be documented as an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the original. In this case, the new items have separate identities. Matter is preserved, but identity is not.
    3. When the initial identity of the changed instance of E18 Physical Thing is preserved, the event should be documented as an instance of E11 Modification.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E6_Destruction"
    P13_destroyed: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P13_destroyed"})


class E7_Activity(E5_Event):
    """Activity <http://www.cidoc-crm.org/cidoc-crm/E7_Activity>.

    This class comprises actions intentionally carried out by instances of E39 Actor that result in changes of state in the cultural, social, or physical systems documented.
    This notion includes complex, composite and long-lasting actions such as the building of a settlement or a war, as well as simple, short-lived actions such as the opening of a door.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E7_Activity"
    P125_used_object_of_type: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P125_used_object_of_type"})
    P134_continued: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P134_continued"})
    P134i_was_continued_by: E7_Activity | list[E7_Activity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P134i_was_continued_by"})
    P14_carried_out_by: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P14_carried_out_by"})
    P15_was_influenced_by: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P15_was_influenced_by"})
    P16_used_specific_object: E70_Thing | list[E70_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P16_used_specific_object"})
    P17_was_motivated_by: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P17_was_motivated_by"})
    P19_was_intended_use_of: E71_Human_Made_Thing | list[E71_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P19_was_intended_use_of"})
    P20_had_specific_purpose: E5_Event | list[E5_Event] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P20_had_specific_purpose"})
    P21_had_general_purpose: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P21_had_general_purpose"})
    P32_used_general_technique: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P32_used_general_technique"})
    P33_used_specific_technique: E29_Design_or_Procedure | list[E29_Design_or_Procedure] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P33_used_specific_technique"})


class E10_Transfer_of_Custody(E7_Activity):
    """Transfer of Custody <http://www.cidoc-crm.org/cidoc-crm/E10_Transfer_of_Custody>.

    This class comprises transfers of the physical custody or the legal responsibility for the physical custody of objects. The recording of the donor or recipient is optional. It is possible that in an instance of E10 Transfer of Custody there is either no donor or no recipient.
    Depending on the circumstances, it may describe:.
    1. the beginning of custody (there is no previous custodian).
    2. the end of custody (there is no subsequent custodian).
    3. the transfer of custody (transfer from one custodian to the next).
    4. the receipt of custody from an unknown source (the previous custodian is unknown).
    5. the declared loss of an object (the current or subsequent custodian is unknown).
    In the event that only a single kind of transfer of custody occurs, either the legal responsibility for the custody or the actual physical possession of the object but not both, this difference should be expressed using the property P2 has type (is type of).
    The sense of physical possession requires that the object of custody be in the hands of the keeper at least with a part representative for the whole. The way, in which a representative part is defined, should ensure that it is unambiguous who keeps a part and who the whole and should be consistent with the identity criteria of the kept instance of E18 Physical Thing.
    The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore models legal ownership and physical custody separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.
    Theft is a specific case of illegal transfer of custody.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E10_Transfer_of_Custody"
    P28_custody_surrendered_by: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P28_custody_surrendered_by"})
    P29_custody_received_by: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P29_custody_received_by"})
    P30_transferred_custody_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P30_transferred_custody_of"})


class E11_Modification(E7_Activity):
    """Modification <http://www.cidoc-crm.org/cidoc-crm/E11_Modification>.

    This class comprises instances of E7 Activity that are undertaken to create, alter or change instances of E24 Physical Human-Made Thing.
    This class includes the production of an item from raw materials and other so far undocumented objects. It also includes the conservation treatment of an object.
    Since the distinction between modification and production is not always clear, modification is regarded as the more generally applicable concept. This implies that some items may be consumed or destroyed in an instance of E11 Modification, and that others may be produced as a result of it. An event should also be documented using an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the originals. In this case, the new items have separate identities.
    An activity undertaken on an object which was designed to alter it, but which, in fact, it did not in any seemingly significant way (such as the application of a solvent during conservation which failed to dissolve any part of the object), is still considered as an instance of E11 Modification. Typically, any such activity will leave at least forensic traces of evidence on the object.
    If the instance of E29 Design or Procedure utilized for the modification prescribes the use of specific materials, they should be documented using property P68 foresees use of (use foreseen by): E57 Material of E29 Design or Procedure, rather than via P126 employed (was employed in): E57 Material.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E11_Modification"
    P126_employed: E57_Material | list[E57_Material] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P126_employed"})
    P31_has_modified: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P31_has_modified"})


class E12_Production(E11_Modification, E63_Beginning_of_Existence):
    """Production <http://www.cidoc-crm.org/cidoc-crm/E12_Production>.

    This class comprises activities that are designed to, and succeed in, creating one or more new items.
    It specializes the notion of modification into production. The decision as to whether or not an object is regarded as new is context sensitive. Normally, items are considered “new” if there is no obvious overall similarity between them and the consumed items and material used in their production. In other cases, an item is considered “new” because it becomes relevant to documentation by a modification. For example, the scribbling of a name on a potsherd may make it a voting token. The original potsherd may not be worth documenting, in contrast to the inscribed one.
    This entity can be collective: the printing of a thousand books, for example, would normally be considered a single event.
    An event should also be documented using an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the originals. In this case, the new items have separate identities and matter is preserved, but identity is not.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E12_Production"
    P108_has_produced: E24_Physical_Human_Made_Thing | list[E24_Physical_Human_Made_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P108_has_produced"})
    P186_produced_thing_of_product_type: E99_Product_Type | list[E99_Product_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P186_produced_thing_of_product_type"})


class E13_Attribute_Assignment(E7_Activity):
    """Attribute Assignment <http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment>.

    This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts. The type of the property asserted to hold between two items or concepts can be described by the property P177 assigned property of type (is type of property assigned): E55 Type.
    For example, the class describes the actions of people making propositions and statements during certain scientific/scholarly procedures, e.g., the person and date when a condition statement was made, an identifier was assigned, the museum object was measured, etc. Which kinds of such assignments and statements need to be documented explicitly in structures of a schema rather than free text, depends on whether this information should be accessible by structured queries.
    This class allows for the documentation of how the respective assignment came about, and whose opinion it was. Note that all instances of properties described in a knowledge base are the opinion of someone. Per default, they are the opinion of the team maintaining the knowledge base. This fact must not individually be registered for all instances of properties provided by the maintaining team, because it would result in an endless recursion of whose opinion was the description of an opinion. Therefore, the use of instances of E13 Attribute Assignment marks the fact, that the maintaining team is in general neutral to the validity of the respective assertion, but registers someone else’s opinion and how it came about.
    All properties assigned in such an action can also be seen as directly relating the respective pair of items or concepts. Multiple use of instances of E13 Attribute Assignment may possibly lead to a collection of contradictory values.
    All cases of properties in this model that are also described indirectly through a subclass of E13 Attribute Assignment are characterised as "short cuts" of a path via this subclass. This redundant modelling of two alternative views is preferred because many implementations may have good reasons to model either the action of assertion or the short cut, and the relation between both alternatives can be captured by simple rules.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment"
    P140_assigned_attribute_to: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P140_assigned_attribute_to"})
    P141_assigned: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P141_assigned"})
    P177_assigned_property_of_type: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P177_assigned_property_of_type"})


class E14_Condition_Assessment(E13_Attribute_Assignment):
    """Condition Assessment <http://www.cidoc-crm.org/cidoc-crm/E14_Condition_Assessment>.

    This class describes the act of assessing the state of preservation of an object during a particular period.
    The condition assessment may be carried out by inspection, measurement or through historical research. This class is used to document circumstances of the respective assessment that may be relevant to interpret its quality at a later stage, or to continue research on related documents.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E14_Condition_Assessment"
    P34_concerned: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P34_concerned"})
    P35_has_identified: E3_Condition_State | list[E3_Condition_State] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P35_has_identified"})


class E15_Identifier_Assignment(E13_Attribute_Assignment):
    """Identifier Assignment <http://www.cidoc-crm.org/cidoc-crm/E15_Identifier_Assignment>.

    This class comprises activities that result in the allocation of an identifier to an instance of E1 CRM Entity. Instances of E15 Identifier Assignment may include the creation of the identifier from multiple constituents, which themselves may be instances of E41 Appellation. The syntax and kinds of constituents to be used may be declared in a rule constituting an instance of E29 Design or Procedure.
    Examples of such identifiers include Find Numbers, Inventory Numbers, uniform titles in the sense of librarianship and Digital Object Identifiers (DOI). Documenting the act of identifier assignment and deassignment is especially useful when objects change custody or the identification system of an organization is changed. In order to keep track of the identity of things in such cases, it is important to document by whom, when and for what purpose an identifier is assigned to an item.
    The fact that an identifier is a preferred one for an organisation can be expressed by using the property E1 CRM Entity. P48 has preferred identifier (is preferred identifier of): E42 Identifier. It can better be expressed in a context independent form by assigning a suitable E55 Type, such as “preferred identifier assignment”, to the respective instance of E15 Identifier Assignment via the P2 has type property.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E15_Identifier_Assignment"
    P142_used_constituent: E90_Symbolic_Object | list[E90_Symbolic_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P142_used_constituent"})
    P37_assigned: E42_Identifier | list[E42_Identifier] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P37_assigned"})
    P38_deassigned: E42_Identifier | list[E42_Identifier] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P38_deassigned"})


class E16_Measurement(E13_Attribute_Assignment):
    """Measurement <http://www.cidoc-crm.org/cidoc-crm/E16_Measurement>.

    This class comprises actions measuring quantitative physical properties and other values that can be determined by a systematic, objective procedure of direct observation of particular states of physical reality.
    An instance of E16 Measurement may use simple counting or tools, such as yardsticks or radiation detection devices. The interest is in the method and care applied, so that the reliability of the result may be judged at a later stage, or research continued on the associated documents. The date of the event is important for dimensions, which may change value over time, such as the length of an object subject to shrinkage. Methods and devices employed should be associated with instances of E16 Measurement by properties such as P33 used specific technique: E29 Design or Procedure, P125 used object of type: E55 Type, P16 used specific object (was used for): E70 Thing, whereas basic techniques such as "carbon-14 dating" should be encoded using P2 has type (is type of): E55 Type. Details of methods and devices reused or reusable in other instances of E16 Measurement should be documented for these entities rather than the measurements themselves, whereas details of particular execution may be documented by free text or by instantiating adequate sub-activities, if the detail may be of interest for an overarching query.
    Regardless whether a measurement is made by an instrument or by human senses, it represents the initial transition from physical reality to information without any other documented information object in between within the reasoning chain that would represent the result of the interaction of the observer or device with reality. Therefore, determining properties of an instance of E90 Symbolic Object is regarded as an instance of E13 Attribute Assignment, which may be inferred from observing and measuring representative carriers. In the case that the carrier can be named, the property P16 used specific object (was used for): should be used to indicate the instance(s) of E18 Physical Thing that was used as the empirical basis for the attribute assignment. For instance, inferring properties of depicted items using image material, such as satellite images, is not regarded as an instance of E16 Measurement, but as a subsequent instance of E13 Attribute Assignment. Rather, only the production of the images, understood as arrays of radiation intensities, is regarded as an instance of E16 Measurement. The same reasoning holds for other sensor data.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E16_Measurement"
    P39_measured: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P39_measured"})
    P40_observed_dimension: E54_Dimension | list[E54_Dimension] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P40_observed_dimension"})


class E17_Type_Assignment(E13_Attribute_Assignment):
    """Type Assignment <http://www.cidoc-crm.org/cidoc-crm/E17_Type_Assignment>.

    This class comprises the actions of classifying items of whatever kind. Such items include objects, specimens, people, actions and concepts.
    This class allows for the documentation of the context of classification acts in cases where the value of the classification depends on the personal opinion of the classifier, and the date that the classification was made. This class also encompasses the notion of "determination," i.e., the systematic and molecular identification of a specimen in biology.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E17_Type_Assignment"
    P41_classified: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P41_classified"})
    P42_assigned: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P42_assigned"})


class E65_Creation(E7_Activity, E63_Beginning_of_Existence):
    """Creation <http://www.cidoc-crm.org/cidoc-crm/E65_Creation>.

    This class comprises events that result in the creation of conceptual items or immaterial products, such as legends, poems, texts, music, images, movies, laws, types etc.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E65_Creation"
    P94_has_created: E28_Conceptual_Object | list[E28_Conceptual_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P94_has_created"})


class E66_Formation(E7_Activity, E63_Beginning_of_Existence):
    """Formation <http://www.cidoc-crm.org/cidoc-crm/E66_Formation>.

    This class comprises events that result in the formation of a formal or informal E74 Group of people, such as a club, society, association, corporation or nation.
    E66 Formation does not include the arbitrary aggregation of people who do not act as a collective.
    The formation of an instance of E74 Group does not require that the group is populated with members at the time of formation. In order to express the joining of members at the time of formation, the respective activity should be simultaneously an instance of both E66 Formation and E85 Joining.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E66_Formation"
    P151_was_formed_from: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P151_was_formed_from"})
    P95_has_formed: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P95_has_formed"})


class E79_Part_Addition(E11_Modification):
    """Part Addition <http://www.cidoc-crm.org/cidoc-crm/E79_Part_Addition>.

    This class comprises activities that result in an instance of E18 Physical Thing being increased, enlarged or augmented by the addition of a part.
    Typical scenarios include the attachment of an accessory, the integration of a component, the addition of an element to an aggregate object, or the accessioning of an object into a curated instance of E78 Curated Holding. Both the E18 Physical Thing being augmented and the E18 Physical Thing that is being added are treated as separate identifiable wholes prior to the instance of E79 Part Addition. Following the addition of parts, the resulting assemblages are treated objectively as single identifiable wholes, made up of constituent or component parts bound together either physically (for example the engine becoming a part of the car), or by sharing a common purpose (such as the 32 chess pieces that make up a chess set). This class of activities forms a basis for reasoning about the history and continuity of identity of objects that are integrated into other objects over time, such as precious gemstones being repeatedly incorporated into different items of jewellery, or cultural artefacts being added to different museum instances of E78 Curated Holding over their lifespan..
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E79_Part_Addition"
    P110_augmented: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P110_augmented"})
    P111_added: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P111_added"})


class E80_Part_Removal(E11_Modification):
    """Part Removal <http://www.cidoc-crm.org/cidoc-crm/E80_Part_Removal>.

    This class comprises the activities that result in an instance of E18 Physical Thing being decreased by the removal of a part.
    Typical scenarios include the detachment of an accessory, the removal of a component or part of a composite object, or the deaccessioning of an object from a curated collection, an instance of E78 Curated Holding. If the instance of E80 Part Removal results in the total decomposition of the original object into pieces, such that the whole ceases to exist, the activity should instead be modelled as an instance of E81 Transformation, i.e., a simultaneous destruction and production. In cases where the part removed has no discernible identity prior to its removal but does have an identity subsequent to its removal, the activity should be modelled as both an instance of E80 Part Removal and E12 Production. This class of activities forms a basis for reasoning about the history, and continuity of identity over time, of objects that are removed from other objects, such as precious gemstones being extracted from different items of jewellery, or cultural artifacts being deaccessioned from different museum collections over their lifespan.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E80_Part_Removal"
    P112_diminished: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P112_diminished"})
    P113_removed: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P113_removed"})


class E81_Transformation(E63_Beginning_of_Existence, E64_End_of_Existence):
    """Transformation <http://www.cidoc-crm.org/cidoc-crm/E81_Transformation>.

    This class comprises the events that result in the simultaneous destruction of one or more than one E18 Physical Thing and the creation of one or more than one E18 Physical Thing that preserves recognizable substance and structure from the first one(s) but has fundamentally different nature or identity.
    Although the old and the new instances of E18 Physical Thing are treated as discrete entities having separate, unique identities, they are causally connected through the E81 Transformation; the destruction of the old E18 Physical Thing(s) directly causes the creation of the new one(s) using or preserving some relevant substance and structure. Instances of E81 Transformation are therefore distinct from re-classifications (documented using E17 Type Assignment) or modifications (documented using E11 Modification) of objects that do not fundamentally change their nature or identity. Characteristic cases are reconstructions and repurposing of historical buildings or ruins, fires leaving buildings in ruins, taxidermy of specimen in natural history.
    Even though such instances of E81 Transformation are often motivated by a change of intended use, substantial material changes should justify the documentation of the result as a new instance of E18 Physical Thing and not just the change of function. The latter may be documented as an extended activity (instance of E7 Activity) of using it.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E81_Transformation"
    P123_resulted_in: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P123_resulted_in"})
    P124_transformed: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P124_transformed"})


class E83_Type_Creation(E65_Creation):
    """Type Creation <http://www.cidoc-crm.org/cidoc-crm/E83_Type_Creation>.

    This class comprises activities formally defining new types of items.
    It is typically a rigorous scholarly or scientific process that ensures a type is exhaustively described and appropriately named. In some cases, particularly in archaeology and the life sciences, E83 Type Creation requires the identification of an exemplary specimen and the publication of the type definition in an appropriate scholarly forum. The activity modelled as an instance of E83 Type Creation is central to research in the life sciences, where a type would be referred to as a “taxon,” the type description as a “protologue,” and the exemplary specimens as “original element” or “holotype”.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E83_Type_Creation"
    P135_created_type: E55_Type | list[E55_Type] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P135_created_type"})
    P136_was_based_on: E1_CRM_Entity | list[E1_CRM_Entity] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P136_was_based_on"})


class E85_Joining(E7_Activity):
    """Joining <http://www.cidoc-crm.org/cidoc-crm/E85_Joining>.

    This class comprises the activities that result in an instance of E39 Actor becoming a member of an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.
    Typical scenarios include becoming a member of a social organisation, becoming employee of a company, marriage, the adoption of a child by a family and the inauguration of somebody into an official position.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E85_Joining"
    P143_joined: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P143_joined"})
    P144_joined_with: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P144_joined_with"})


class E86_Leaving(E7_Activity):
    """Leaving <http://www.cidoc-crm.org/cidoc-crm/E86_Leaving>.

    This class comprises the activities that result in an instance of E39 Actor to be disassociated from an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.
    Typical scenarios include the termination of membership in a social organisation, ending the employment at a company, divorce, and the end of tenure of somebody in an official position.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E86_Leaving"
    P145_separated: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P145_separated"})
    P146_separated_from: E74_Group | list[E74_Group] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P146_separated_from"})


class E87_Curation_Activity(E7_Activity):
    """Curation Activity <http://www.cidoc-crm.org/cidoc-crm/E87_Curation_Activity>.

    This class comprises the activities that result in the continuity of management and the preservation and evolution of instances of E78 Curated Holding, following an implicit or explicit curation plan.
    It specializes the notion of activity into the curation of a collection and allows the history of curation to be recorded.
    Items are accumulated and organized following criteria like subject, chronological period, material type, style of art etc. and can be added or removed from an instance of E78 Curated Holding for a specific purpose and/or audience. The initial aggregation of items of a collection is regarded as an instance of E12 Production Event while the activity of evolving, preserving and promoting a collection is regarded as an instance of E87 Curation Activity.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E87_Curation_Activity"
    P147_curated: E78_Curated_Holding | list[E78_Curated_Holding] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P147_curated"})


class E8_Acquisition(E7_Activity):
    """Acquisition <http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition>.

    This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more other instances of E39 Actor.
    The class also applies to the establishment or loss of ownership of instances of E18 Physical Thing. It does not, however, imply changes of any other kinds of right. The recording of the donor and/or recipient is optional. It is possible that in an instance of E8 Acquisition there is either no donor or no recipient. Depending on the circumstances, it may describe:.
    1. the beginning of ownership.
    2. the end of ownership.
    3. the transfer of ownership.
    4. the acquisition from an unknown source.
    5. the loss of title due to destruction of the item.
    It may also describe events where a collector appropriates legal title, for example by annexation or field collection. The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore models legal ownership (E8 Acquisition) and physical custody (E10 Transfer of Custody) separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition"
    P22_transferred_title_to: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P22_transferred_title_to"})
    P23_transferred_title_from: E39_Actor | list[E39_Actor] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P23_transferred_title_from"})
    P24_transferred_title_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P24_transferred_title_of"})


class E93_Presence(E92_Spacetime_Volume):
    """Presence <http://www.cidoc-crm.org/cidoc-crm/E93_Presence>.

    This class comprises instances of E92 Spacetime Volume, whose temporal extent has been chosen in order to determine the spatial extent of a phenomenon over the chosen time-span. Respective phenomena may, for instance, be historical events or periods, but can also be the diachronic extent and existence of physical things. In other words, instances of this class fix a slice of another instance of E92 Spacetime Volume in time.
    The temporal extent of an instance of E93 Presence typically is predetermined by the researcher so as to focus the investigation particularly on finding the spatial extent of the phenomenon by testing for its characteristic features. There are at least two basic directions such investigations might take. The investigation may wish to determine where something was during some time or it may wish to reconstruct the total passage of a phenomenon’s spacetime volume through an examination of discrete presences. Observation and measurement of features indicating the presence or absence of a phenomenon in some space allows for the progressive approximation of spatial extents through argumentation typically based on inclusion, exclusion and various overlaps.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E93_Presence"
    P164_is_temporally_specified_by: E52_Time_Span | list[E52_Time_Span] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P164_is_temporally_specified_by"})
    P166_was_a_presence_of: E92_Spacetime_Volume | list[E92_Spacetime_Volume] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P166_was_a_presence_of"})
    P167_was_within: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P167_was_within"})
    P195_was_a_presence_of: E18_Physical_Thing | list[E18_Physical_Thing] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P195_was_a_presence_of"})
    P197_covered_parts_of: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P197_covered_parts_of"})


class E96_Purchase(E8_Acquisition):
    """Purchase <http://www.cidoc-crm.org/cidoc-crm/E96_Purchase>.

    This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more different instances of E39 Actor, where the transferring party is completely compensated by the payment of a monetary amount. In more detail, a purchase agreement establishes a fixed monetary obligation at its initialization on the receiving party, to the giving party. An instance of E96 Purchase begins with the contract or equivalent agreement and ends with the fulfilment of all contractual obligations. In the case that the activity is abandoned before both parties have fulfilled these obligations, the activity is not regarded as an instance of E96 Purchase.
    This class is a very specific case of the much more complex social business practices of exchange of goods and the creation and satisfaction of related social obligations. Purchase activities which define individual sales prices per object can be modelled by instantiating E96 Purchase for each object individually and as part of an overall instance of E96 Purchase transaction.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E96_Purchase"
    P179_had_sales_price: E97_Monetary_Amount | list[E97_Monetary_Amount] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P179_had_sales_price"})


class E97_Monetary_Amount(E54_Dimension):
    """Monetary Amount <http://www.cidoc-crm.org/cidoc-crm/E97_Monetary_Amount>.

    This class comprises quantities of monetary possessions or obligations in terms of their nominal value with respect to a particular currency. These quantities may be abstract accounting units, the nominal value of a heap of coins or bank notes at the time of validity of the respective currency, the nominal value of a bill of exchange or other documents expressing monetary claims or obligations. It specifically excludes amounts expressed in terms of weights of valuable items, like gold and diamonds, and quantities of other non-currency items, like goats or stocks and bonds.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E97_Monetary_Amount"
    P179i_was_sales_price_of: E96_Purchase | list[E96_Purchase] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P179i_was_sales_price_of"})
    P180_has_currency: E98_Currency | list[E98_Currency] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P180_has_currency"})


class E98_Currency(E58_Measurement_Unit):
    """Currency <http://www.cidoc-crm.org/cidoc-crm/E98_Currency>.

    This class comprises the units in which a monetary system, supported by an administrative authority or other community, quantifies and arithmetically compares all monetary amounts declared in the unit. The unit of a monetary system must describe a nominal value which is kept constant by its administrative authority and an associated banking system if it exists, and not by market value. For instance, one may pay with grams of gold, but the respective monetary amount would have been agreed as the gold price in US dollars on the day of the payment. Under this definition, British Pounds, U.S. Dollars, and European Euros are examples of currency, but “grams of gold” is not. One monetary system has one and only one currency. Instances of this class must not be confused with coin denominations, such as “Dime” or “Sestertius”. Non-monetary exchange of value in terms of quantities of a particular type of goods, such as cows, do not constitute a currency.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E98_Currency"
    P180i_was_currency_of: E97_Monetary_Amount | list[E97_Monetary_Amount] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P180i_was_currency_of"})


class E99_Product_Type(E55_Type):
    """Product Type <http://www.cidoc-crm.org/cidoc-crm/E99_Product_Type>.

    This classes comprises types that stand as the models for instances of E22 Human-Made Object that are produced as the result of production activities using plans exact enough to result in one or more series of uniform, functionally and aesthetically identical and interchangeable items. The product type is the intended ideal form of the manufacture process. It is typical of instances of E22 that conform to an instance of E99 Product Type that its component parts are interchangeable with component parts of other instances of E22 made after the model of the same instance of E99. Frequently, the uniform production according to a given instance of E99 Product Type is achieved by creating individual tools, such as moulds or print plates that are themselves carriers of the design of the product type. Modern tools may use the flexibility of electronically controlled devices to achieve such uniformity. The product type itself, i.e., the potentially unlimited series of aesthetically equivalent items, may be the target of artistic design, rather than the individual object. In extreme cases, only one instance of a product type may have been produced, such as in a "print on demand" process which was only triggered once. However, this should not be confused with industrial prototypes, such as car prototypes, which are produced prior to the production line being set up, or test the production line itself.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E99_Product_Type"
    P186i_is_produced_by: E12_Production | list[E12_Production] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P186i_is_produced_by"})
    P187_has_production_plan: E29_Design_or_Procedure | list[E29_Design_or_Procedure] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P187_has_production_plan"})
    P188_requires_production_tool: E19_Physical_Object | list[E19_Physical_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P188_requires_production_tool"})


class E9_Move(E7_Activity):
    """Move <http://www.cidoc-crm.org/cidoc-crm/E9_Move>.

    This class comprises changes of the physical location of the instances of E19 Physical Object.
    Note, that the class E9 Move inherits the property P7 took place at (witnessed): E53 Place. This property should be used to describe the trajectory or a larger area within which a move takes place, whereas the properties P26 moved to (was destination of), P27 moved from (was origin of) describe the start and end points only. Moves may also be documented to consist of other moves (via P9 consists of (forms part of)), in order to describe intermediate stages on a trajectory. In that case, start and end points of the partial moves should match appropriately between each other and with the overall event.
    """
    _class_iri: ClassVar[str] = "http://www.cidoc-crm.org/cidoc-crm/E9_Move"
    P25_moved: E19_Physical_Object | list[E19_Physical_Object] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P25_moved"})
    P26_moved_to: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P26_moved_to"})
    P27_moved_from: E53_Place | list[E53_Place] | None = Field(default=None, json_schema_extra={"_property_iri": "http://www.cidoc-crm.org/cidoc-crm/P27_moved_from"})

