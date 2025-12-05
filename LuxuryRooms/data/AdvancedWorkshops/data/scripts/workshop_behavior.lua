-- Advanced Workshop Behavior Script
-- Manages workshop equipment efficiency and prisoner skill development

local workshop_multipliers = {
    Woodworking = 2.0,
    Electronics = 2.5,
    Metalworking = 2.2,
    Textile = 1.8
}

function onWorkshopStart(prisoner, equipment)
    local prisoner_skill = prisoner:getSkill('craftsmanship') or 0
    local efficiency_bonus = prisoner_skill * 0.1
    equipment:setEfficiency(1.0 + efficiency_bonus)
end

function onWorkshopComplete(prisoner, equipment, duration)
    -- Increase prisoner craftsmanship skill
    local current_skill = prisoner:getSkill('craftsmanship') or 0
    local skill_increase = duration * 0.05
    prisoner:setSkill('craftsmanship', current_skill + skill_increase)
    
    -- Calculate reward multiplier
    local equipment_name = equipment:getName()
    local base_reward = 100
    local multiplier = workshop_multipliers[equipment_name] or 1.0
    local final_reward = base_reward * multiplier
    
    return final_reward
end

function getWorkshopProductivity(equipment, prisoners)
    local total_productivity = 0
    for _, prisoner in ipairs(prisoners) do
        local skill = prisoner:getSkill('craftsmanship') or 0
        local mood = prisoner:getMood()
        local productivity = (skill * 0.5) + (mood * 0.5)
        total_productivity = total_productivity + productivity
    end
    return total_productivity / #prisoners
end
