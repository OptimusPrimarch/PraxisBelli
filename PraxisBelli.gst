<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gameSystem id="sys-cd5a-2de6-f8aa-24ee" name="PraxisBelli" battleScribeVersion="2.03" revision="1" type="gameSystem" xmlns="http://www.battlescribe.net/schema/gameSystemSchema">
  <categoryEntries>
    <categoryEntry name="Armor" id="7681-e699-f10a-e57b" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Bulwark" id="fd49-38eb-bfa6-c130" hidden="false" type="rule" targetId="e7f9-3ad7-5bf1-b1b0"/>
        <infoLink name="Hardpoints" id="18f6-3c9f-8550-997a" hidden="false" type="rule" targetId="b4f5-fc33-99b2-10f1"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Command" id="c892-1e80-87b3-2ee2" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Leadership Aura" id="1fc6-d164-423d-dce8" hidden="false" type="rule" targetId="92ca-3761-4367-8623"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Line" id="9bdf-0174-74ef-f0af" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Boots on the Ground" id="3606-8f95-6cd7-3f5d" hidden="false" type="rule" targetId="7b4f-5341-0942-c2f6"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Recon" id="e06d-3eb6-2edc-cee7" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Spotter" id="213a-567f-5fe3-e10b" hidden="false" type="rule" targetId="f2b2-cc37-b7b6-5eab"/>
        <infoLink name="Camouflaged" id="4431-baf8-fc68-af57" hidden="false" type="rule" targetId="1ebc-c239-c7ec-a794"/>
        <infoLink name="All-Terrain" id="8fa1-2326-750b-993a" hidden="false" type="rule" targetId="28c6-c562-0bd6-a469"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Shock" id="49f8-be80-6328-d7dc" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Brutal Assault" id="8031-254d-6d11-18b5" hidden="false" type="rule" targetId="e53b-b8b7-2e89-6d6f"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Support" id="aa80-441a-6103-d793" hidden="false">
      <description>Force Organization Keyword</description>
      <infoLinks>
        <infoLink name="Where We&apos;re Needed" id="a174-c758-2ad6-f0e9" hidden="false" type="rule" targetId="b703-78a5-41d4-d72e"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Infantry" id="0855-9c5c-35f4-04c1" hidden="false">
      <infoLinks>
        <infoLink name="Entrenched" id="9232-acda-c2e4-cdff" hidden="false" type="rule" targetId="9f10-8dad-4a5b-71f4"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Cavalry" id="2ab8-78f7-b507-dd19" hidden="false">
      <infoLinks>
        <infoLink name="Run Them Through" id="d931-8a64-bc32-608f" hidden="false" type="rule" targetId="cd1d-eeb0-c67d-3b2e"/>
        <infoLink name="All-Terrain" id="f2e9-f2b6-e1ff-2a2d" hidden="false" type="rule" targetId="28c6-c562-0bd6-a469"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Vehicle" id="4e41-bd1a-1e9f-f591" hidden="false">
      <infoLinks>
        <infoLink name="Armored Front" id="f094-adf6-971f-49ec" hidden="false" type="rule" targetId="670f-bca7-b3e7-f8b2"/>
        <infoLink name="Hardpoints" id="1485-b8b1-479f-ebab" hidden="false" type="rule" targetId="b4f5-fc33-99b2-10f1"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Monster" id="18b8-e55b-7c93-8700" hidden="false">
      <infoLinks>
        <infoLink name="Terrifying" id="c72b-4985-14d5-242f" hidden="false" type="rule" targetId="4e70-077c-1136-4bb8"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Aerial" id="c4e5-9b9b-cb06-7d59" hidden="false">
      <infoLinks>
        <infoLink name="Flying" id="c9d9-3e6b-9c0f-6d3e" hidden="false" type="rule" targetId="cba3-21e4-5394-9575"/>
        <infoLink name="Soaring Above" id="ca5a-1d83-2ff1-737f" hidden="false" type="rule" targetId="ce02-664a-e8b6-8939"/>
      </infoLinks>
    </categoryEntry>
    <categoryEntry name="Towable" id="ee57-adfd-29c9-10b9" hidden="false">
      <infoLinks>
        <infoLink name="Trailor" id="0705-ed06-572e-a1e4" hidden="false" type="rule" targetId="3326-d259-05fa-c38f"/>
        <infoLink name="Emplaced Weapon" id="d096-137d-9bbc-dc52" hidden="false" type="rule" targetId="053e-0e77-d08d-080a"/>
      </infoLinks>
    </categoryEntry>
  </categoryEntries>
  <costTypes>
    <costType name="Roster Points" id="3ef7-040e-27e8-40c1" defaultCostLimit="-1"/>
  </costTypes>
  <profileTypes>
    <profileType name="Unit Profile" id="c6e9-1c16-74f0-2b58" hidden="false" kind="model">
      <characteristicTypes>
        <characteristicType name="Speed" id="56e8-b0fe-53d2-3faf"/>
        <characteristicType name="Mettle" id="e1e4-ceec-a5b1-60d3"/>
        <characteristicType name="Evasion" id="c0fb-48d3-2f02-fa09"/>
        <characteristicType name="Armor" id="8e9e-b2d4-8d48-d4d0"/>
        <characteristicType name="Toughness" id="4a8a-2752-aa8a-d5e3"/>
      </characteristicTypes>
    </profileType>
    <profileType name="Weapon Profile" id="2555-341b-f64e-0ff7" hidden="false" kind="weapon">
      <characteristicTypes>
        <characteristicType name="Range" id="74c2-5191-931e-1f4a" defaultValue="M"/>
        <characteristicType name="Attacks" id="b7ab-77b3-5293-37ad" defaultValue="1"/>
        <characteristicType name="Armor Piercing" id="b2af-eca3-b6be-cd79" defaultValue="0"/>
        <characteristicType name="Damage" id="7d08-d823-3c78-0fc3" defaultValue="1"/>
        <characteristicType name="Weapon Traits" id="ed87-b9c1-459b-efb1" kind="longText"/>
      </characteristicTypes>
    </profileType>
  </profileTypes>
  <sharedRules>
    <rule name="Blast (S)" id="916e-0e5e-526b-21a4" hidden="false">
      <description>This weapon can target a point instead of a model, and centers a circular blast template on that point if the to-hit roll succeeds. If the to-hit roll is missed, roll a 1d5 and scatter the point of impact in the direction it&apos;s pointing a number of inches equal to the result. Targets affected by the blast cannot benefit from cover.</description>
    </rule>
    <rule name="Blast (L)" id="8c45-fc64-8fa0-fbf1" hidden="false">
      <description>This weapon can target a point instead of a model, and centers a circular blast template on that point if the to-hit roll succeeds. If the to-hit roll is missed, roll a 1d10 and scatter the point of impact in the direction it&apos;s pointing a number of inches equal to the result. Targets affected by the blast cannot benefit from cover.</description>
    </rule>
    <rule name="Accurate" id="a3c9-2224-49f9-297a" hidden="false">
      <description>When shooting with this weapon, ignore all range penalties.</description>
    </rule>
    <rule name="Pistol" id="2ec2-2bea-ba0c-98d2" hidden="false">
      <description>This weapon can be used to make a ranged attack while the bearer is engaged, but it must target an enemy unit it&apos;s engaged with.</description>
    </rule>
    <rule name="Regeneration" id="5c44-7340-c533-1419" hidden="false">
      <description>At the end of every round, this unit regains 1d5 lost wounds.</description>
    </rule>
    <rule name="Entrenched" id="9f10-8dad-4a5b-71f4" hidden="false">
      <description>While in cover, this unit gains an additional +1 ARM and rerolls failed Mettle checks.</description>
    </rule>
    <rule name="Run Them Through" id="cd1d-eeb0-c67d-3b2e" hidden="false">
      <description>This units&apos; weapons gain +1AP and Suppressing whenever it is charging.</description>
    </rule>
    <rule name="Armored Front" id="670f-bca7-b3e7-f8b2" hidden="false">
      <description>This unit uses 90-degree facings to signify the front, back, left, and right sides. Attacks targeting the vehicles front are made with -1AP. Attacks targeting the vehicles rear are made with +1AP.</description>
    </rule>
    <rule name="Leadership Aura" id="92ca-3761-4367-8623" hidden="false">
      <description>Units within 12&quot; of this model may use its MET instead of their own when making Mettle checks.</description>
    </rule>
    <rule name="Terrifying" id="4e70-077c-1136-4bb8" hidden="false">
      <description>Units that end their activation engaged with this one are forced to make a Mettle check.</description>
    </rule>
    <rule name="Flying" id="cba3-21e4-5394-9575" hidden="false">
      <description>This model may ignore other models and terrain while it is moving.</description>
    </rule>
    <rule name="Soaring Above" id="ce02-664a-e8b6-8939" hidden="false">
      <description>When this unit activates, it immediately moves half of its Speed, after which it continues its activation as normal. This unit may move off the table edge; if it does so, remove it from play and redeploy it in its same state in the owner&apos;s deployment zone. This unit may only be charged by enemy units with Flying.</description>
    </rule>
    <rule name="Spotter" id="f2b2-cc37-b7b6-5eab" hidden="false">
      <description>This unit fulfills the requirement for Indirect Fire or Guided weapons. In addition, it ignores the effects of smoke.</description>
    </rule>
    <rule name="Bulwark" id="e7f9-3ad7-5bf1-b1b0" hidden="false">
      <description>Whenever this unit takes damage, reduce the damage by 1 (to a minimum of 1).</description>
    </rule>
    <rule name="Boots on the Ground" id="7b4f-5341-0942-c2f6" hidden="false">
      <description>This unit does not need to spend an action to claim an objective.</description>
    </rule>
    <rule name="Anti-Aerial" id="dd9a-3f66-5b9e-86fa" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Armor" id="4057-f400-8ea9-db3e" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Cavalry" id="cc10-40eb-2758-1d2e" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Command" id="aa48-92c6-6cd2-469c" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Infantry" id="7801-ef6a-9919-421b" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Line" id="8da6-739b-911d-27ca" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Monster" id="b916-1651-9632-c933" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Recon" id="e9cd-e108-6c16-5b2c" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Shock" id="61ce-0077-43ab-e867" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Support" id="1219-4f34-83e5-155a" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Towable" id="c94b-2be8-fd3e-7b32" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Anti-Vehicle" id="6802-8c4b-3ea8-d1f3" hidden="false">
      <description>When this weapon makes damage rolls against a target with the listed keyword, each successful damage roll counts as two hits instead of one. Because hits are allocated individually, the additional hits may spill onto other models in the target unit.</description>
    </rule>
    <rule name="Trailor" id="3326-d259-05fa-c38f" hidden="false">
      <description>This unit can spend an action to hitch to a friendly VEHICLE within 3&quot; of it. It will have to spend an action to unhitch at a later point.</description>
    </rule>
    <rule name="Emplaced Weapon" id="053e-0e77-d08d-080a" hidden="false">
      <description>This unit must spend an action to correctly deploy itself before it is capable of making ranged attacks. It is immobile while emplaced.</description>
    </rule>
    <rule name="Where We&apos;re Needed" id="b703-78a5-41d4-d72e" hidden="false">
      <description>This unit treats every 2&quot; traveled as consuming only 1&quot; of its Speed while within its own Deployment Zone.</description>
    </rule>
    <rule name="Brutal Assault" id="e53b-b8b7-2e89-6d6f" hidden="false">
      <description>This unit rerolls hit results of 1 when fighting or shooting within half range.</description>
    </rule>
    <rule name="Transport (11)" id="5664-3c9f-debe-8bc6" hidden="false">
      <description>This unit can carry up to 11 models with the INFANTRY or CAVALRY keyword. Embarking and disembarking are both part of a Move action and cost half the embarking unit&apos;s Speed, rounding up; a unit must begin its embark within 1&quot; of this one, and disembarks into base contact with it before resolving any remaining movement. While embarked, a unit does not contest or claim objectives, and all measurement to or from it is taken from this model. If this model is removed from play, every embarked model must pass a Mettle check or suffer 1 wound; survivors are placed within 3&quot; of the wreck.</description>
    </rule>
    <rule name="Transport (14)" id="e63e-876f-efc0-efb5" hidden="false">
      <description>This unit can carry up to 14 models with the INFANTRY or CAVALRY keyword. Embarking and disembarking are both part of a Move action and cost half the embarking unit&apos;s Speed, rounding up; a unit must begin its embark within 1&quot; of this one, and disembarks into base contact with it before resolving any remaining movement. While embarked, a unit does not contest or claim objectives, and all measurement to or from it is taken from this model. If this model is removed from play, every embarked model must pass a Mettle check or suffer 1 wound; survivors are placed within 3&quot; of the wreck.</description>
    </rule>
    <rule name="Transport (6)" id="b9ec-fe2d-ea71-a758" hidden="false">
      <description>This unit can carry up to 6 models with the INFANTRY or CAVALRY keyword. Embarking and disembarking are both part of a Move action and cost half the embarking unit&apos;s Speed, rounding up; a unit must begin its embark within 1&quot; of this one, and disembarks into base contact with it before resolving any remaining movement. While embarked, a unit does not contest or claim objectives, and all measurement to or from it is taken from this model. If this model is removed from play, every embarked model must pass a Mettle check or suffer 1 wound; survivors are placed within 3&quot; of the wreck.</description>
    </rule>
    <rule name="Transport (28)" id="136d-3202-3258-ebd9" hidden="false">
      <description>This unit can carry up to 28 models with the INFANTRY or CAVALRY keyword. Embarking and disembarking are both part of a Move action and cost half the embarking unit&apos;s Speed, rounding up; a unit must begin its embark within 1&quot; of this one, and disembarks into base contact with it before resolving any remaining movement. While embarked, a unit does not contest or claim objectives, and all measurement to or from it is taken from this model. If this model is removed from play, every embarked model must pass a Mettle check or suffer 1 wound; survivors are placed within 3&quot; of the wreck.</description>
    </rule>
    <rule name="Open-Topped" id="0a1c-77b5-4e23-9d80" hidden="false">
      <description>Units embarked in this Transport may still take actions, measuring range and line of sight from this model. In exchange, an embarked unit is independently targetable whenever line of sight can be drawn to this model, using its own EVA and ARM rather than this model&apos;s, and counts as being in Cover while it does so.</description>
    </rule>
    <rule name="Closed-Topped" id="4f27-9e11-b6a8-31cd" hidden="false">
      <description>Units embarked in this Transport may take no actions except the Move action used to disembark, and cannot be targeted while embarked. Attacks may only be directed at this model.</description>
    </rule>
    <rule name="Indirect" id="c1d8-5a92-7f04-b6e3" hidden="false">
      <description>This weapon may target an enemy unit without line of sight, provided an allied unit with the Spotter rule has line of sight to that target. Attacks made this way suffer no penalty for the firing model&apos;s own lack of line of sight.</description>
    </rule>
    <rule name="Smoke" id="8b3e-c604-d179-2f5a" hidden="false">
      <description>A smoke marker blocks line of sight drawn through it, exactly as Blocking terrain does, until the end of the round in which it was placed. Units with the Spotter rule ignore its effects.</description>
    </rule>
    <rule name="Engulf (S)" id="e00d-1348-3f1f-bd09" hidden="false">
      <description>This weapon uses a small teardrop template; its targets can&apos;t benefit from cover.</description>
    </rule>
    <rule name="Engulf (L)" id="813b-6058-8182-a5c6" hidden="false">
      <description>This weapon uses a large teardrop template; its targets can&apos;t benefit from cover.</description>
    </rule>
    <rule name="Fearless" id="7f7a-eca2-04a2-f10f" hidden="false">
      <description>This model and its unit ignore suppression markers when making Mettle checks. In addition, it ignores the negative effects of deteriorating morale unless it is Routing.</description>
    </rule>
    <rule name="Guided" id="c7f2-8464-aafc-b17e" hidden="false">
      <description>If this weapon&apos;s target is visible to an allied RECON unit, decrease the target&apos;s EVA by 3. Disregard any additional modifiers.</description>
    </rule>
    <rule name="Heavy" id="5553-344a-75e2-a122" hidden="false">
      <description>This weapon can&apos;t make attacks in the same activation its unit moved in; if the unit attacks first, it is then unable to move.</description>
    </rule>
    <rule name="Hardpoints" id="b4f5-fc33-99b2-10f1" hidden="false">
      <description>Ignore the effect of the HEAVY weapon trait.</description>
    </rule>
    <rule name="Camouflaged" id="1ebc-c239-c7ec-a794" hidden="false">
      <description>While in cover, this unit gains an additional +1EVA.</description>
    </rule>
    <rule name="All-Terrain" id="28c6-c562-0bd6-a469" hidden="false">
      <description>This unit ignores difficult terrain penalties.</description>
    </rule>
    <rule name="Turret" id="f28a-17c0-d122-e5e3" hidden="false">
      <description>This weapon can be fired from any facing.</description>
    </rule>
    <rule name="Frontal Arc" id="7097-aee9-4b71-f90b" hidden="false">
      <description>This weapon can only be used against targets in the bearer&apos;s front facing.</description>
    </rule>
    <rule name="Rear Arc" id="fab0-ef6e-377f-53ce" hidden="false">
      <description>This weapon can only be used against targets in the bearer&apos;s rear facing.</description>
    </rule>
    <rule name="Side Arc" id="0cd7-6a66-f65b-4e7b" hidden="false">
      <description>This weapon can only be used against targets in the bearer&apos;s side facings.</description>
    </rule>
    <rule name="Suppressing" id="4b66-483e-c75a-6c01" hidden="false">
      <description>Targets of this weapon&apos;s attacks gain a suppression marker, regardless of the outcome of the attack.</description>
    </rule>
    <rule name="Coaxial" id="93e8-2589-f3df-0ce0" hidden="false">
      <description>This weapon must target the same target as the weapon listed in the annotation.</description>
    </rule>
    <rule name="Linked-Weapon" id="cd4f-1017-04d8-c017" hidden="false">
      <description>Reroll all misses when attacking with this weapon.</description>
    </rule>
  </sharedRules>
</gameSystem>
