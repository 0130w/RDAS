use crate::utils::{parser, structures::{BusinessInfo, FilterConditions, Position, SortConditions}};


pub fn view_business(business_id: String) -> Option<BusinessInfo>{
    let path = "dataset/rec_business.json";
    let businesses : Vec<BusinessInfo> = parser::parse_json(path);
    for business in businesses {
        if business_id == business.business_id {
            return Some(business) 
        }
    }
    None
}

#[allow(unused)]
pub fn sort_business(sort_condition: SortConditions, position: Position) -> Vec<BusinessInfo>{
    let path = 
        match sort_condition {
            SortConditions::Synthesis => {
                "dataset/sort_business_by_synthesis.json"
            },
            SortConditions::Distance => {
                "dataset/sort_business_by_dis.json"
            },
            SortConditions::Stars => {
                "dataset/sort_business_by_stars.json"
            }
        };
    let mut businesses : Vec<BusinessInfo> = parser::parse_json(path);
    businesses
}

#[allow(unused)]
pub fn filter_business(filter_condition: FilterConditions) {
    
}