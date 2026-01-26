from importlib import import_module
__all__: list[str] = []

_CLASS_TO_MODULE = {
    'TransferOfCustody': '.crm.E10_Transfer_of_Custody',
    'Modification': '.crm.E11_Modification',
    'Production': '.crm.E12_Production',
    'AttributeAssignment': '.crm.E13_Attribute_Assignment',
    'ConditionAssessment': '.crm.E14_Condition_Assessment',
    'IdentifierAssignment': '.crm.E15_Identifier_Assignment',
    'Measurement': '.crm.E16_Measurement',
    'TypeAssignment': '.crm.E17_Type_Assignment',
    'PhysicalThing': '.crm.E18_Physical_Thing',
    'PhysicalObject': '.crm.E19_Physical_Object',
    'CRMEntity': '.crm.E1_CRM_Entity',
    'BiologicalObject': '.crm.E20_Biological_Object',
    'Person': '.crm.E21_Person',
    'HumanMadeObject': '.crm.E22_Human_Made_Object',
    'PhysicalHumanMadeThing': '.crm.E24_Physical_Human_Made_Thing',
    'HumanMadeFeature': '.crm.E25_Human_Made_Feature',
    'PhysicalFeature': '.crm.E26_Physical_Feature',
    'Site': '.crm.E27_Site',
    'ConceptualObject': '.crm.E28_Conceptual_Object',
    'DesignOrProcedure': '.crm.E29_Design_or_Procedure',
    'TemporalEntity': '.crm.E2_Temporal_Entity',
    'Right': '.crm.E30_Right',
    'Document': '.crm.E31_Document',
    'AuthorityDocument': '.crm.E32_Authority_Document',
    'Name': '.crm.E33_E41_Linguistic_Appellation',
    'LinguisticObject': '.crm.E33_Linguistic_Object',
    'Inscription': '.crm.E34_Inscription',
    'Title': '.crm.E35_Title',
    'VisualItem': '.crm.E36_Visual_Item',
    'Mark': '.crm.E37_Mark',
    'Actor': '.crm.E39_Actor',
    'ConditionState': '.crm.E3_Condition_State',
    'Appellation': '.crm.E41_Appellation',
    'Identifier': '.crm.E42_Identifier',
    'Period': '.crm.E4_Period',
    'TimeSpan': '.crm.E52_Time_Span',
    'Place': '.crm.E53_Place',
    'Dimension': '.crm.E54_Dimension',
    'Type': '.crm.E55_Type',
    'Language': '.crm.E56_Language',
    'Material': '.crm.E57_Material',
    'MeasurementUnit': '.crm.E58_Measurement_Unit',
    'Event': '.crm.E5_Event',
    'BeginningOfExistence': '.crm.E63_Beginning_of_Existence',
    'EndOfExistence': '.crm.E64_End_of_Existence',
    'Creation': '.crm.E65_Creation',
    'Formation': '.crm.E66_Formation',
    'Birth': '.crm.E67_Birth',
    'Dissolution': '.crm.E68_Dissolution',
    'Death': '.crm.E69_Death',
    'Destruction': '.crm.E6_Destruction',
    'Thing': '.crm.E70_Thing',
    'HumanMadeThing': '.crm.E71_Human_Made_Thing',
    'LegalObject': '.crm.E72_Legal_Object',
    'InformationObject': '.crm.E73_Information_Object',
    'Group': '.crm.E74_Group',
    'PersistentItem': '.crm.E77_Persistent_Item',
    'CuratedHolding': '.crm.E78_Curated_Holding',
    'PartAddition': '.crm.E79_Part_Addition',
    'Activity': '.crm.E7_Activity',
    'PartRemoval': '.crm.E80_Part_Removal',
    'Transformation': '.crm.E81_Transformation',
    'TypeCreation': '.crm.E83_Type_Creation',
    'Joining': '.crm.E85_Joining',
    'Leaving': '.crm.E86_Leaving',
    'CurationActivity': '.crm.E87_Curation_Activity',
    'PropositionalObject': '.crm.E89_Propositional_Object',
    'Acquisition': '.crm.E8_Acquisition',
    'SymbolicObject': '.crm.E90_Symbolic_Object',
    'SpacetimeVolume': '.crm.E92_Spacetime_Volume',
    'Presence': '.crm.E93_Presence',
    'Purchase': '.crm.E96_Purchase',
    'MonetaryAmount': '.crm.E97_Monetary_Amount',
    'Currency': '.crm.E98_Currency',
    'ProductType': '.crm.E99_Product_Type',
    'Move': '.crm.E9_Move',
    'Addition': '.la.Addition',
    'DigitalService': '.la.DigitalService',
    'Payment': '.la.Payment',
    'Removal': '.la.Removal',
    'RightAcquisition': '.la.RightAcquisition',
    'Set': '.la.Set',
    'Transfer': '.la.Transfer',
}

__all__ = sorted(_CLASS_TO_MODULE.keys())
_PREFIXES = sorted({path.split('.')[1] for path in _CLASS_TO_MODULE.values()})
_REBUILT = False

def _load_all_and_rebuild():
    global _REBUILT
    if _REBUILT:
        return
    _modules = []
    for _prefix in _PREFIXES:
        mod = import_module(f'.{_prefix}', __name__)
        _modules.append(mod)
    _types_namespace: dict[str, object] = {}
    for _module in _modules:
        for _name in getattr(_module, '__all__', []):
            _obj = getattr(_module, _name, None)
            if _obj is None:
                continue
            globals()[_name] = _obj
            _types_namespace[_name] = _obj
    for _obj in _types_namespace.values():
        _rebuild = getattr(_obj, 'model_rebuild', None)
        if _rebuild:
            _rebuild(_types_namespace=_types_namespace, recurse=True)
    _REBUILT = True

def __getattr__(name: str):
    if not _REBUILT:
        _load_all_and_rebuild()
    obj = globals().get(name)
    if obj is not None:
        return obj
    module_path = _CLASS_TO_MODULE.get(name)
    if module_path is None:
        raise AttributeError(name)
    mod = import_module(module_path, __name__)
    obj = getattr(mod, name)
    globals()[name] = obj  # cache
    return obj

def __dir__():
    return sorted(__all__ + list(globals().keys()))

_load_all_and_rebuild()
