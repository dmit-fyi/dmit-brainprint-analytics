#!/usr/bin/env python3
"""
DMIT BrainPrint Analytics
An intelligent assessment platform for fingerprint analysis, cognitive profiling,
learning preferences, personality insights, and career guidance.
Guided by Mrs. Priyanka Swain, Founder of Merit Teacher.
https://dmit.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "brain_print": "BrainPrint",
        "cognitive_profile": "Cognitive Profile",
        "learning_style": "Learning Style",
        "personality_insight": "Personality Insight",
        "career_pathway": "Career Pathway",
        "leadership_workplace": "Leadership & Workplace",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_multiple_intelligence(cognitive: int, learning: int, personality: int) -> dict:
    return {
        "Logical-Mathematical": min(100, round(cognitive * 1.07)),
        "Linguistic": min(100, round(cognitive * 1.0)),
        "Spatial-Visual": min(100, round(learning * 1.0)),
        "Interpersonal": min(100, round(personality * 1.03)),
    }


def analyze_brainprint(
    profile: str,
    assessment_type: str = "student-dmit",
    brain_print: int = 88,
    cognitive_profile: int = 82,
    learning_style: int = 85,
    personality_insight: int = 78,
    career_pathway: int = 90,
    leadership_workplace: int = 80,
) -> dict:
    """
    Analyze DMIT BrainPrint assessment signals.

    Args:
        profile: Individual profile identifier
        assessment_type: Type of DMIT assessment
        brain_print: BrainPrint fingerprint score (0-100)
        cognitive_profile: Cognitive profile score (0-100)
        learning_style: Learning style score (0-100)
        personality_insight: Personality insight score (0-100)
        career_pathway: Career pathway score (0-100)
        leadership_workplace: Leadership and workplace score (0-100)

    Returns:
        dict with individual signal scores, overall BrainPrint index,
        and multiple intelligence profile
    """
    scores = {
        "brain_print": brain_print,
        "cognitive_profile": cognitive_profile,
        "learning_style": learning_style,
        "personality_insight": personality_insight,
        "career_pathway": career_pathway,
        "leadership_workplace": leadership_workplace,
    }
    overall_brainprint_index = round(sum(scores.values()) / 6)

    return {
        "profile": profile,
        "assessment_type": " ".join(w.capitalize() for w in assessment_type.split("-")),
        "brain_print_score": brain_print,
        "cognitive_profile_score": cognitive_profile,
        "learning_style_score": learning_style,
        "personality_insight_score": personality_insight,
        "career_pathway_score": career_pathway,
        "leadership_workplace_score": leadership_workplace,
        "overall_brainprint_index": overall_brainprint_index,
        "priority_action": get_priority_action(scores),
        "multiple_intelligence": get_multiple_intelligence(cognitive_profile, learning_style, personality_insight),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    profile = args[0] if len(args) > 0 else "student-profile"
    assessment_type = args[1] if len(args) > 1 else "student-dmit"
    brain_print = int(args[2]) if len(args) > 2 else 88
    cognitive_profile = int(args[3]) if len(args) > 3 else 82
    learning_style = int(args[4]) if len(args) > 4 else 85
    personality_insight = int(args[5]) if len(args) > 5 else 78
    career_pathway = int(args[6]) if len(args) > 6 else 90
    leadership_workplace = int(args[7]) if len(args) > 7 else 80

    result = analyze_brainprint(
        profile, assessment_type, brain_print, cognitive_profile,
        learning_style, personality_insight, career_pathway, leadership_workplace
    )

    print(f"Profile: {result['profile']}")
    print(f"Assessment Type: {result['assessment_type']}")
    print("=" * 45)
    print(f"BrainPrint Score:              {result['brain_print_score']}/100  [{get_status(result['brain_print_score'])}]")
    print(f"Cognitive Profile Score:       {result['cognitive_profile_score']}/100  [{get_status(result['cognitive_profile_score'])}]")
    print(f"Learning Style Score:          {result['learning_style_score']}/100  [{get_status(result['learning_style_score'])}]")
    print(f"Personality Insight Score:     {result['personality_insight_score']}/100  [{get_status(result['personality_insight_score'])}]")
    print(f"Career Pathway Score:          {result['career_pathway_score']}/100  [{get_status(result['career_pathway_score'])}]")
    print(f"Leadership & Workplace Score:  {result['leadership_workplace_score']}/100  [{get_status(result['leadership_workplace_score'])}]")
    print("=" * 45)
    print(f"Overall BrainPrint Index:      {result['overall_brainprint_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nMultiple Intelligence Profile:")
    for intel, score in result['multiple_intelligence'].items():
        print(f"  {intel:<28} {score}/100")


if __name__ == "__main__":
    main()
